import os


def scan_folder(folder_path):
    # get the items inside the folder 
    # Display the items
    items = os.listdir(folder_path)
    
    for item in items:
        print(f"ITEM: {item}")
    pass

