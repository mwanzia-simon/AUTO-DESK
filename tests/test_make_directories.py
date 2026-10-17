import os
import shutil

folder_path = "C:/Users/dell/Desktop/AutoDeskTest"

source = os.path.join(folder_path,"my_file.txt")
destination = os.path.join(folder_path,"Documents","my_file.txt")

shutil.move(source,destination)
