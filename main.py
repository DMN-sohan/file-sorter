import os, shutil, time, json

downloads_path = "C:\\Users\\Sohan\\Downloads"

def check_type(full_path):
    return_type = {
        ".pdf" : "pdf_path",
        ".docx" : "doc_path",
        ".pptx" : "ppt_path",
        ".mkv" : "video_path",
        ".mp4" : "video_path",
        ".zip" : "zip_path",
        ".rar" : "zip_path", 
        ".tar.gz" : "zip_path",
        ".HEIC" : "image_path", 
        ".jpg" : "image_path", 
        ".png" : "image_path", 
        ".ico" : "image_path", 
        ".jpeg" : "image_path", 
        ".jfif" : "image_path",
        ".webp" : "image_path",
        ".exe" : "exe_path",
        ".appx" : "exe_path",
        ".img" : "exe_path",
        ".bat" : "exe_path",
        ".msi" : "exe_path",
        ".opdownload" : "NULL",
        ".crdownload" : "NULL",
        ".opdownload" : "NULL",
        ".download" : "NULL",
        ".part" : "NULL",
        ".temp" : "NULL",
        ".tmp" : "NULL",
        "log.txt" : "NULL"
        }

    for i in return_type.keys():
        if full_path.lower().endswith(i):
            return return_type[i]
    return "misc_path"

def check_directory(path):
    return os.path.isdir(os.path.join(downloads_path,path)) or check_type(path) == "NULL"

def move_file(start_path,end_path):
    try:
        shutil.move(start_path,end_path)
    except:
        pass

def folders_do_exist():
    with open("path.json","r") as f:
        global paths
        paths = json.loads(f.readline())

    for i in paths.values():
        if not os.path.exists(i):
            os.makedirs(i)

    if not os.path.exists(os.path.join(downloads_path,"log.txt")):
        with open(os.path.join(downloads_path,"log.txt"),"w") as f:
            pass

folders_do_exist()

while True:
    time.sleep(5)
    files = [i for i in os.listdir(downloads_path) if not check_directory(i)]
    for file in files:
        with open(os.path.join(downloads_path,"log.txt"),"a") as f:
            f.write(f"Moving {file} into {paths[check_type(file)]}\n")
        move_file(os.path.join(downloads_path,file),paths[check_type(file)])




