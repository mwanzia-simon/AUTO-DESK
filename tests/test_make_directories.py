import os
import shutil

folder_path = "C:/Users/dell/Desktop/AutoDeskTest"

source = os.path.join(folder_path,"sample.txt")
destination = os.path.join(folder_path,"Documents","sample.txt")

shutil.move(source,destination)
