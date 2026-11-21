"""
Package the final university submission and project ZIP files without presentation files.
Course: CSE471 | Submission Archive
Authors:
  - Sahil Kumar (1245740)
  - Amit Singh Sikarwar (12409171)
  - Chahak Singh (12502965)
"""

import os
import zipfile
import shutil

def package_all():
    base_dir = "e:/CSE471"
    
    # Root files to include: ONLY main project files and updated documentation (NO presentation files)
    files_to_include = [
        "README.md",
        ".gitignore",
        "Deployment_Link.txt",
        "IEEE_AgriGuard_Project_Documentation.pdf",
        "IEEE_AgriGuard_Project_Documentation.docx",
        "IEEE_AgriGuard_Project_Documentation.md",
        "RollNo_CropDiseaseDetection_Report.pdf"
    ]
    
    dirs_to_include = [
        "Code",
        "Data"
    ]
    
    # Target zip archives to create
    target_zips = [
        os.path.join(base_dir, "RollNo_CropDiseaseDetection.zip"),
        os.path.join(base_dir, "AgriGuard-Crop-Disease-Detection-and-Management.zip")
    ]
    
    primary_zip = target_zips[0]
    print(f"Creating clean project archive: {primary_zip}...")
    
    with zipfile.ZipFile(primary_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
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
                # Exclude temporary, cache, git, and presentation files
                dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", "real_plantdoc_kaggle", "real_plantdoc")]
                for f in files:
                    if f.endswith(('.pptx', '.ppt', '.pyc', '.tmp', '.DS_Store')):
                        continue
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, base_dir)
                    zipf.write(full_p, arcname=rel_p)
                    
    primary_size_mb = os.path.getsize(primary_zip) / (1024 * 1024)
    print(f"\n[AgriGuard] Created: {primary_zip} ({primary_size_mb:.2f} MB)")
    
    # Copy to repo-named release archive
    repo_zip = target_zips[1]
    shutil.copyfile(primary_zip, repo_zip)
    repo_size_mb = os.path.getsize(repo_zip) / (1024 * 1024)
    print(f"[AgriGuard] Created: {repo_zip} ({repo_size_mb:.2f} MB)")
    
    return target_zips

if __name__ == '__main__':
    package_all()
