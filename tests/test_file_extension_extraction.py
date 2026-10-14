import os

file1 = "report.pdf"
file2 = "report.final.compiled.pdf"

name,extension = os.path.splitext(file1)

print(name)
print(extension)

print(os.path.splitext(file2))