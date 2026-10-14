import os
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

file = "profile.png"

extension = os.path.splitext(file)[1].lower()

if extension in file_types["Images"]:
    print("This is an image.")