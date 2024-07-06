import os
import shutil
dir = os.path.join(os.path.expanduser("~"), "I miei file")
extensions = {
    "jpg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "py": "Python codes",
    "c": "C codes",
    "mp4": "Videos",
    "mp3": "Audios",
}
source_dir = "File/I miei file/File Linux/Download"
with os.scandir(source_dir) as files:
    
    for file in files:
        if file.is_file():
            name = file.name
            extension = name.split(".")[-1]
            if extension in extensions:
                destination = extensions[extension]

                if not os.path.exists(f"{dir}/{destination}"):
                    os.makedirs(f"{dir}/{destination}")
                    shutil.move((os.path.join(source_dir,name), f"{dir}/{destination}/{name}"))
            elif extension not in extensions:
                if not os.path.exists(f"{dir}/Others"):
                    os.makedirs(f"{dir}/Others")
                shutil.move((os.path.join(source_dir,name), f"{dir}/Others/{name}"))