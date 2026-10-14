import os

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx",".js",".ts"],
    "Videos": [".mp4", ".mkv", ".mov"],
}
folder_path = "C:/Users/dell/Desktop/CODING/MERN STACK PROJECTS/CAMPUS-MARKETPLACE/client"

files = os.listdir(folder_path)



for file in files:
    full_path = os.path.join(folder_path,file)
    if os.path.isfile(full_path):
        file_category = "Unknown file type"
        file_extension = os.path.splitext(file)[1].lower()
        for category, extensions in file_types.items():
            if file_extension in extensions:
                file_category = category
                print(f"{file} --> Category: {file_category}")
                break
