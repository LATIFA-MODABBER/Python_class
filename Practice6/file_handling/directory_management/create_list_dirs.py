import os
import shutil

# ---------- Create nested directories ----------
nested_dir = "../python/Practice6/directoy_management"
os.makedirs(nested_dir, exist_ok=True)
print("Nested directories created.")


# ---------- List files and folders ----------
print("\nListing current directory:")
for item in os.listdir("."):
    print(item)


# ---------- Find files by extension ----------
print("\nFinding .txt files:")
for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)


