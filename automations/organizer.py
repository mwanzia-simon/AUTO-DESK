import os

folder_path = "C:/Users/dell/Desktop/AutoDeskTest/Documents"


def scan_folder(folder_path):
    items = os.listdir(folder_path)
    
    for item in items:
        full_path = os.path.join(folder_path,item)
        if os.path.isfile(full_path):
            print(f"FILE: {item}")
        if os.path.isdir(full_path):
            print(f"FOLDER: {item}")

scan_folder(folder_path)

