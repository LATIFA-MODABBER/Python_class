import shutil


shutil.copy("Sample.txt", "Backup.txt")
print("Backup created successfully.")

import os 
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exists. ")