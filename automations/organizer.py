import os

folder_path = "C:/Users/dell/Desktop/AutoDeskTest/Documents"

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".js", ".ts"],
    "Videos": [".mp4", ".mkv", ".mov"]
}


def scan_folder(folder_path):
    items = os.listdir(folder_path)
    
    for item in items:
        full_path = os.path.join(folder_path,item)
        if os.path.isfile(full_path):
            file_category = "Unknown file type"
            file_extension = os.path.splitext(item)[1].lower()
            for category, extensions in file_types.items():
                        if file_extension in extensions:
                            file_category = category
                            print(f"FILE: {item} --> Category: {file_category}")
        if os.path.isdir(full_path):
            print(f"FOLDER: {item}")

scan_folder(folder_path)

