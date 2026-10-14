import os
folder_path = "C:/Users/dell/Desktop/CODING/MERN STACK PROJECTS/CAMPUS-MARKETPLACE/client"

items = os.listdir(folder_path)

for item in items:
    full_path = os.path.join(folder_path,item)
    if os.path.isfile(full_path):
        print(f"{item} is a file.")
    elif os.path.isdir(full_path):
        print(f"{item} is a folder.")