import shutil

with open("Sample.txt", "r") as file:
    print(file.read())
with open("Sample.txt", "a") as file:
    file.write("Customer ID: 1005 \n")
    file.write("Name: Zinab\n")
    file.write("City: Boston\n")
    file.write("Purchase: Smartwatch\n")

with open("Sample.txt", "r") as file:
    print("\n updated File:")
    print(file.read())

shutil.copy("Sample.txt", "Backup.txt")
print("Backup created successfully.")

import os 
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exists. ")