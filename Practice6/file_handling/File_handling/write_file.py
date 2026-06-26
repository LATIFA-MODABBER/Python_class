import shutil
import os

with open("Sample.txt", "a") as file:
    file.write("Customer ID: 1005 \n")
    file.write("Name: Zinab\n")
    file.write("City: Boston\n")
    file.write("Purchase: Smartwatch\n")

with open("Sample.txt", "r") as file:
    print("\n updated File:")
    print(file.read())
