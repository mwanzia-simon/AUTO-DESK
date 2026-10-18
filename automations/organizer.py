import os
import shutil

folder_path = "C:/Users/dell/Desktop/AutoDeskTest/Documents"

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".js", ".ts"],
    "Videos": [".mp4", ".mkv", ".mov"]
}


def scan_folder(folder_path):
    try:
        items = os.listdir(folder_path)
    except FileNotFoundError:
        print("Invalid Path!")
        return 0,0,0
    except PermissionError:
        print("Access Denied!")
        return 0,0,0
    
    moved_count = 0
    skipped_count = 0
    failed_count = 0
    
    for item in items:
        full_path = os.path.join(folder_path,item)
        if os.path.isfile(full_path):
            file_category = "Unknown file type"
            file_extension = os.path.splitext(item)[1].lower()
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    file_category = category
                    break
            print(f"FILE: {item} --> Category: {file_category}")
            if file_category != "Unknown file type":
                
                try:
                    os.makedirs(os.path.join(folder_path,file_category),exist_ok=True)
                except OSError as error:
                    print(f"Could not create folder {file_category} : {error}")
                    failed_count += 1
                    continue
                
                source = os.path.join(folder_path,item)
                destination = os.path.join(folder_path,file_category,item)
                
                if os.path.exists(destination):
                    print(f"Skipped {item}: File already Exists!")
                    skipped_count += 1
                else:
                    try:
                        shutil.move(source,destination)
                        moved_count += 1
                    except OSError as error:
                        print(f"Could not move {item} : {error}")
                        failed_count += 1
                
        elif os.path.isdir(full_path):
            print(f"FOLDER: {item}")
    return moved_count,skipped_count,failed_count
   

if __name__ == "__main__":
    moved,skipped,failed = scan_folder(folder_path)
    print(f"Moved: {moved}")
    print(f"Skipped: {skipped}")
    print(f"Failed: {failed}")

