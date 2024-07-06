import os
import shutil
dir = os.path.join(os.path.expanduser("~"), "Download")
extensions = {
    "jpg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "py": "Python codes",
    "c": "C codes",
    "mp4": "Videos",
}
source_dir = "File/I miei file/Download "
with os.scandir(source_dir) as files:
    
    for file in files:
        name = file.name
        extension = name.split(".")[-1]
        if name.endswith(extensions):
            shutil.move(os.path.join(source_dir / name), extensions[extension])