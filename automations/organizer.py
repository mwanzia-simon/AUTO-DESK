import os

folder_path = "C:/Users/dell/Desktop/AutoDeskTest/Documents"


def scan_folder(folder_path):
    items = os.listdir(folder_path)
    
    for item in items:
        print(f"ITEM: {item}")
    pass

scan_folder(folder_path)

