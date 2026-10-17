import os
import shutil

folder_path = "C:/Users/dell/Desktop/AutoDeskTest/Images"

source = ""
destination = ""

shutil.move(source,destination)

os.makedirs(folder_path,exist_ok=True)