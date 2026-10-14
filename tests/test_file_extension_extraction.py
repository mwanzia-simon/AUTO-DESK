import os

folder_path = "C:/Users/dell/Desktop/CODING/MERN STACK PROJECTS/CAMPUS-MARKETPLACE/client"

files = os.listdir(folder_path)

for file in files:
    full_path = os.path.join(folder_path,file)
    if os.path.isfile(full_path):
        extension = os.path.splitext(file)[1]
        if extension == "":
            extension = "No extension"
        print(f"{file} -> Extension:{extension}")