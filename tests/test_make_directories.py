import os
import shutil

folder_path = "C:/Users/dell/Desktop/AutoDeskTest/Images"

source = "C:/Users/dell/Desktop/AutoDeskTest/sample.txt"
destination = "C:/Users/dell/Desktop/AutoDeskTest/Documents/sample.txt"

shutil.move(source,destination)

os.makedirs(folder_path,exist_ok=True)