import os

file = "report.pdf"

name,extension = os.path.splitext(file)

print(name)
print(extension)