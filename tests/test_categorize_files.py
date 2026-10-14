import os
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

file = "profile.png"

file_extension = os.path.splitext(file)[1].lower()

# if extension in file_types["Images"]:
#     print("This is an image.")

for category,extensions in file_types.items():
   if file_extension in file_types[category]:
       print(f"{file} --> Category: {category}")
   else:
       print("Unknown file type")