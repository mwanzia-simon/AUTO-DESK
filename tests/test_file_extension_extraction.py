import os

files = ["report.pdf","my_photo.jpeg","assignment.docx","logo.png"]

# file1 = "report.pdf"
# file2 = "report.final.compiled.pdf"

# name,extension = os.path.splitext(file1)

# print(name)
# print(extension)
# print(os.path.splitext(file2))

for file in files:
    print(f"{file} -> Extension: {os.path.splitext(file)[1]}")