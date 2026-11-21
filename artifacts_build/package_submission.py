"""
Package the final university submission ZIP file.
Course: CSE471 | Submission Archive
"""

import os
import zipfile

def package_submission(zip_filename="e:/CSE471/RollNo_CropDiseaseDetection.zip"):
    base_dir = "e:/CSE471"
    
    # Items to include in the root of the ZIP
    files_to_include = [
        "RollNo_CropDiseaseDetection_Report.pdf",
        "RollNo_CropDiseaseDetection_PPT.pptx",
        "Deployment_Link.txt",
        "IEEE_AgriGuard_Project_Documentation.pdf",
        "IEEE_AgriGuard_Project_Documentation.docx",
        "IEEE_AgriGuard_Project_Documentation.md"
    ]
    
    dirs_to_include = [
        "Code",
        "Data"
    ]
    
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add root files
        for fname in files_to_include:
            fpath = os.path.join(base_dir, fname)
            if os.path.exists(fpath):
                zipf.write(fpath, arcname=fname)
                print(f"Added file: {fname}")
            else:
                print(f"Warning: File not found: {fpath}")
                
        # Add directories recursively
        for dname in dirs_to_include:
            dpath = os.path.join(base_dir, dname)
            for root, dirs, files in os.walk(dpath):
                # Ignore __pycache__, .git, and huge multi-gigabyte raw download caches for LMS compliance
                dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", "real_plantdoc_kaggle", "real_plantdoc")]
                for f in files:
                    if f.endswith(('.pyc', '.tmp', '.DS_Store')):
                        continue
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, base_dir)
                    zipf.write(full_p, arcname=rel_p)
                    print(f"Added: {rel_p}")
                    
    zip_size_mb = os.path.getsize(zip_filename) / (1024 * 1024)
    print(f"\n[AgriGuard] Final Submission ZIP packaged successfully: {zip_filename} ({zip_size_mb:.2f} MB)")

if __name__ == '__main__':
    package_submission()

