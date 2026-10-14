import os

folder_path = "C:/Users/dell/Desktop/CODING/MERN STACK PROJECTS/CAMPUS-MARKETPLACE/client"

files = os.listdir(folder_path)

for file in files:
    full_path = os.path.join(folder_path,file)
    extension = ""
    if os.path.isfile(full_path):
        if os.path.splitext(file)[1] != "":
            extension = os.path.splitext(file)[1]
        else:
            extension = "No extension"
        
        print(f"{file} -> Extension:{extension}")