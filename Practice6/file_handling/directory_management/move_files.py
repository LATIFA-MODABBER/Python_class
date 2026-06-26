import shutil
import os

# ---------- Move/copy files between directories ----------
source_file = "sample.txt"
dest_dir = "main_dir"

# Copy file
if os.path.exists(source_file):
    shutil.copy(source_file, os.path.join(dest_dir, source_file))
    print("File copied to directory.")