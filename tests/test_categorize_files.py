import os

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
}

file = "profile.txt"
file_category = "Unknown file type"

file_extension = os.path.splitext(file)[1].lower()

for category, extensions in file_types.items():
    if file_extension in extensions:
        file_category = category
        break

print(f"{file} --> Category: {file_category}")