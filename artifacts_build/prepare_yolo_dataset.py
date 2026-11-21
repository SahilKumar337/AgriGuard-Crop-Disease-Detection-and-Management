"""
Prepare and generate YOLO-format crop disease and pest detection dataset.
Annotates lesion bounding boxes in standard normalized format:
<class_id> <x_center> <y_center> <width> <height>
Course: CSE471 | AIML Engineering Pipeline
"""

import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def generate_yolo_dataset(base_dir="e:/CSE471/Data/yolo_dataset"):
    for split in ['train', 'val', 'test']:
        os.makedirs(os.path.join(base_dir, 'images', split), exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'labels', split), exist_ok=True)

    # Disease generation definitions with exact lesion bounding boxes
    disease_configs = [
        {
            "name": "tomato_early_blight",
            "class_id": 0,
            "spots": [(120, 130, 22), (180, 170, 18), (140, 210, 15), (100, 180, 12)],
            "type": "target_spot"
        },
        {
            "name": "tomato_late_blight",
            "class_id": 1,
            "spots": [(110, 100, 30), (170, 180, 35)],
            "type": "water_soaked"
        },
        {
            "name": "potato_early_blight",
            "class_id": 2,
            "spots": [(130, 140, 20), (160, 200, 18)],
            "type": "target_spot"
        },
        {
            "name": "potato_late_blight",
            "class_id": 3,
            "spots": [(120, 110, 38), (175, 190, 32)],
            "type": "water_soaked"
        },
        {
            "name": "apple_scab",
            "class_id": 4,
            "spots": [(110, 100, 16), (135, 115, 14), (160, 95, 15), (130, 160, 18), (175, 190, 15)],
            "type": "scab"
        },
        {
            "name": "corn_fall_armyworm",
            "class_id": 5,
            "spots": [(125, 135, 25), (170, 175, 20)],
            "type": "pest_hole"
        },
        {
            "name": "rice_brown_spot",
            "class_id": 6,
            "spots": [(130, 120, 14), (160, 170, 12), (120, 200, 10)],
            "type": "oval_spot"
        },
        {
            "name": "wheat_leaf_rust",
            "class_id": 7,
            "spots": [(140, 90, 10), (150, 130, 12), (135, 170, 10), (160, 210, 11)],
            "type": "rust_pustule"
        },
        {
            "name": "grape_black_rot",
            "class_id": 8,
            "spots": [(115, 130, 18), (170, 160, 22)],
            "type": "pycnidia"
        },
        {
            "name": "healthy_crop",
            "class_id": 9,
            "spots": [],
            "type": "healthy"
        }
    ]

    total_samples = 0
    img_size = 320 # Standard image size for training

    for split, count_per_class in [('train', 8), ('val', 3), ('test', 2)]:
        for cfg in disease_configs:
            cid = cfg["class_id"]
            cname = cfg["name"]
            
            for idx in range(count_per_class):
                # Base leaf background with slight random variations
                img = Image.new('RGB', (img_size, img_size), color=(235 + np.random.randint(-10, 10), 242 + np.random.randint(-10, 10), 230))
                draw = ImageDraw.Draw(img)

                # Foliage polygon
                pts = [
                    (160, 30), (240 + np.random.randint(-10, 10), 120),
                    (260 + np.random.randint(-10, 10), 200), (190, 290),
                    (160, 305), (130, 290),
                    (60 + np.random.randint(-10, 10), 200), (80 + np.random.randint(-10, 10), 120)
                ]
                draw.polygon(pts, fill=(45 + np.random.randint(-5, 10), 140 + np.random.randint(-10, 10), 50))
                # Midrib
                draw.line([(160, 30), (160, 305)], fill=(80, 180, 70), width=4)

                bboxes = []

                # Draw lesions and record normalized bboxes
                for (cx, cy, r) in cfg["spots"]:
                    # Slight jitter per sample
                    cx_j = max(min(cx + np.random.randint(-8, 8), img_size - 30), 30)
                    cy_j = max(min(cy + np.random.randint(-8, 8), img_size - 30), 30)
                    r_j = max(r + np.random.randint(-3, 3), 8)

                    if cfg["type"] == "target_spot":
                        draw.ellipse([cx_j - r_j - 4, cy_j - r_j - 4, cx_j + r_j + 4, cy_j + r_j + 4], fill=(195, 190, 45))
                        draw.ellipse([cx_j - r_j, cy_j - r_j, cx_j + r_j, cy_j + r_j], fill=(92, 54, 25))
                        draw.ellipse([cx_j - int(r_j*0.5), cy_j - int(r_j*0.5), cx_j + int(r_j*0.5), cy_j + int(r_j*0.5)], fill=(130, 75, 35))
                    elif cfg["type"] == "water_soaked":
                        draw.polygon([(cx_j - r_j, cy_j - r_j), (cx_j + r_j, cy_j - r_j//2), (cx_j + r_j//2, cy_j + r_j), (cx_j - r_j//2, cy_j + r_j//2)], fill=(65, 52, 50))
                    elif cfg["type"] == "scab":
                        draw.ellipse([cx_j - r_j, cy_j - r_j, cx_j + r_j, cy_j + r_j], fill=(42, 58, 30))
                    elif cfg["type"] == "pest_hole":
                        draw.ellipse([cx_j - r_j, cy_j - r_j, cx_j + r_j, cy_j + r_j], fill=(235, 242, 230))
                        draw.ellipse([cx_j - 3, cy_j - 3, cx_j + 3, cy_j + 3], fill=(60, 45, 20))
                    else: # rust/pycnidia/oval
                        draw.ellipse([cx_j - r_j, cy_j - r_j, cx_j + r_j, cy_j + r_j], fill=(180, 85, 25))

                    # Normalized YOLO bbox: <x_center> <y_center> <width> <height>
                    bbox_w = (2 * r_j + 8) / img_size
                    bbox_h = (2 * r_j + 8) / img_size
                    norm_x = cx_j / img_size
                    norm_y = cy_j / img_size
                    bboxes.append(f"{cid} {norm_x:.5f} {norm_y:.5f} {bbox_w:.5f} {bbox_h:.5f}")

                img_filename = f"{cname}_{split}_{idx}.jpg"
                lbl_filename = f"{cname}_{split}_{idx}.txt"

                img_path = os.path.join(base_dir, 'images', split, img_filename)
                lbl_path = os.path.join(base_dir, 'labels', split, lbl_filename)

                img.save(img_path, quality=95)
                with open(lbl_path, 'w') as f_lbl:
                    f_lbl.write("\n".join(bboxes))

                total_samples += 1

    print(f"[AgriGuard] Successfully created YOLO dataset with {total_samples} annotated samples in {base_dir}")

if __name__ == '__main__':
    generate_yolo_dataset()

