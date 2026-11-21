"""
Extract and Setup Full Real PlantDoc Kaggle Dataset for YOLOv8 Training
Sanitizes filenames for Windows filesystem, handles long paths (MAX_PATH), and generates YOLO annotations.
"""
import os
import sys
import re
import csv
import io
import hashlib
import subprocess
import yaml

TARGET_DIR = os.path.abspath("Data/real_plantdoc_kaggle")

def sanitize_filename(name):
    # Remove query params or illegal Windows chars: \ / : * ? " < > |
    clean = re.sub(r'[\?\*:"<>|]', '_', name)
    clean = clean.replace('?itok=', '_itok_').replace('%23', '_').replace('+', '_')
    base, ext = os.path.splitext(clean)
    if len(base) > 60:
        base = base[:50] + "_" + hashlib.md5(clean.encode()).hexdigest()[:8]
    return base + ext

def get_win_path(p):
    abs_p = os.path.abspath(p)
    if os.name == 'nt' and not abs_p.startswith('\\\\?\\'):
        return '\\\\?\\' + abs_p
    return abs_p

def setup_real_dataset():
    print("[Real Kaggle PlantDoc] Initializing extraction from local git object store...")
    if not os.path.exists(os.path.join(TARGET_DIR, ".git")):
        print("Error: .git directory not found in TARGET_DIR.")
        sys.exit(1)

    # 1. Read train_labels.csv and test_labels.csv from git
    train_csv_raw = subprocess.check_output(
        ['git', 'show', 'HEAD:train_labels.csv'], cwd=TARGET_DIR, text=True, encoding='utf-8', errors='ignore'
    )
    test_csv_raw = subprocess.check_output(
        ['git', 'show', 'HEAD:test_labels.csv'], cwd=TARGET_DIR, text=True, encoding='utf-8', errors='ignore'
    )

    train_reader = list(csv.DictReader(io.StringIO(train_csv_raw)))
    test_reader = list(csv.DictReader(io.StringIO(test_csv_raw)))

    # 2. Extract unique class names
    all_classes = set()
    for row in train_reader + test_reader:
        c = row['class'].strip()
        if c:
            all_classes.add(c)
    classes = sorted(list(all_classes))
    class_to_id = {c: i for i, c in enumerate(classes)}
    id_to_class = {i: c for i, c in enumerate(classes)}

    print(f"[Real Kaggle PlantDoc] Found {len(classes)} biological classes:")
    for idx, c in enumerate(classes):
        print(f"  {idx}: {c}")

    # 3. Create target directories
    img_train_dir = os.path.join(TARGET_DIR, "images", "train")
    img_val_dir = os.path.join(TARGET_DIR, "images", "val")
    lbl_train_dir = os.path.join(TARGET_DIR, "labels", "train")
    lbl_val_dir = os.path.join(TARGET_DIR, "labels", "val")

    for d in [img_train_dir, img_val_dir, lbl_train_dir, lbl_val_dir]:
        os.makedirs(get_win_path(d), exist_ok=True)

    # 4. List all blobs in git tree
    tree_out = subprocess.check_output(['git', 'ls-tree', '-r', 'HEAD'], cwd=TARGET_DIR, text=True, encoding='utf-8', errors='ignore')
    blob_map = {}
    for line in tree_out.strip().split('\n'):
        parts = line.strip().split()
        if len(parts) >= 4 and parts[1] == 'blob':
            blob_hash = parts[2]
            filepath = ' '.join(parts[3:])
            blob_map[filepath] = blob_hash

    print(f"[Real Kaggle PlantDoc] Extracting and sanitizing images across {len(blob_map)} repository entries...")

    # Helper to extract images
    extracted_train = 0
    extracted_val = 0
    filename_map = {} # original -> sanitized filename

    for filepath, blob_hash in blob_map.items():
        if filepath.startswith("TRAIN/") and (filepath.lower().endswith('.jpg') or filepath.lower().endswith('.jpeg') or filepath.lower().endswith('.png')):
            orig_name = os.path.basename(filepath)
            clean_name = sanitize_filename(orig_name)
            filename_map[orig_name] = clean_name
            out_path = os.path.join(img_train_dir, clean_name)
            win_p = get_win_path(out_path)
            if not os.path.exists(win_p):
                img_data = subprocess.check_output(['git', 'cat-file', 'blob', blob_hash], cwd=TARGET_DIR)
                with open(win_p, 'wb') as f:
                    f.write(img_data)
            extracted_train += 1

        elif filepath.startswith("TEST/") and (filepath.lower().endswith('.jpg') or filepath.lower().endswith('.jpeg') or filepath.lower().endswith('.png')):
            orig_name = os.path.basename(filepath)
            clean_name = sanitize_filename(orig_name)
            filename_map[orig_name] = clean_name
            out_path = os.path.join(img_val_dir, clean_name)
            win_p = get_win_path(out_path)
            if not os.path.exists(win_p):
                img_data = subprocess.check_output(['git', 'cat-file', 'blob', blob_hash], cwd=TARGET_DIR)
                with open(win_p, 'wb') as f:
                    f.write(img_data)
            extracted_val += 1

    print(f"[Real Kaggle PlantDoc] Extracted {extracted_train} train images and {extracted_val} test/val images.")

    # 5. Convert CSV annotations to YOLO format
    def convert_annotations(rows, out_dir):
        labels_by_img = {}
        for row in rows:
            orig_fname = row['filename'].strip()
            clean_fname = filename_map.get(orig_fname, sanitize_filename(orig_fname))
            txt_name = os.path.splitext(clean_fname)[0] + ".txt"

            cname = row['class'].strip()
            if cname not in class_to_id:
                continue
            cid = class_to_id[cname]

            try:
                w_img, h_img = float(row['width']), float(row['height'])
                xmin, ymin, xmax, ymax = float(row['xmin']), float(row['ymin']), float(row['xmax']), float(row['ymax'])
            except ValueError:
                continue

            if w_img <= 0 or h_img <= 0 or xmax <= xmin or ymax <= ymin:
                continue

            xc = min(max(((xmin + xmax) / 2.0) / w_img, 0.0), 1.0)
            yc = min(max(((ymin + ymax) / 2.0) / h_img, 0.0), 1.0)
            bw = min(max((xmax - xmin) / w_img, 0.0), 1.0)
            bh = min(max((ymax - ymin) / h_img, 0.0), 1.0)

            labels_by_img.setdefault(txt_name, []).append(f"{cid} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")

        for txt_name, lines in labels_by_img.items():
            win_lbl_p = get_win_path(os.path.join(out_dir, txt_name))
            with open(win_lbl_p, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
        return len(labels_by_img)

    n_train_lbls = convert_annotations(train_reader, lbl_train_dir)
    n_val_lbls = convert_annotations(test_reader, lbl_val_dir)
    print(f"[Real Kaggle PlantDoc] Generated {n_train_lbls} train label files and {n_val_lbls} val label files.")

    # 6. Generate dataset.yaml
    yaml_config = {
        'path': TARGET_DIR.replace('\\', '/'),
        'train': 'images/train',
        'val': 'images/val',
        'nc': len(classes),
        'names': id_to_class
    }
    yaml_path = os.path.join(TARGET_DIR, "dataset.yaml")
    with open(get_win_path(yaml_path), 'w', encoding='utf-8') as f:
        yaml.dump(yaml_config, f, default_flow_style=False)

    print(f"[Real Kaggle PlantDoc] Configuration written to: {yaml_path}")
    print("[Real Kaggle PlantDoc] Dataset setup 100% COMPLETE!")

if __name__ == '__main__':
    setup_real_dataset()
