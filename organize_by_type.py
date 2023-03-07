import os
import sys
import hashlib
from pathlib import Path
import shutil


#Creating folders for diff file types:

def create_folders(download_Directory, fileTypes):
    for fileType in fileTypes.keys():
        directory = download_Directory + "\\" + fileType

        if not os.path.exists(directory):
            os.mkdir(directory)



#get checksum of a file

def checkSum(fileDir, chunk_size = 8192):
    md5 = hashlib.md5()    #md5 algo is used to encrypt the file and compare the hash value of src and dest file
    f = open(fileDir)
    while True:
        chunk = f.read(chunk_size)

        if not chunk:
            break
        md5.update(chunk)
    f.close()
    return md5.hexdigest()



#Moving files to appropriate folder and deleting any duplicates if any


def move_files(moveFile,download_Directory,fileTypes):
    if "." in moveFile:
        temp = moveFile.split(".")
        fileFormat = temp[-1]
        fileFormat = fileFormat.lower()

    else:
        return

    for fileType in fileTypes.keys():
        if fileFormat in fileTypes[fileType]:
            src_path = download_Directory + "\\" + moveFile
            dest_path = download_Directory + "\\\\" + moveFile

            print(dest_path)


            if not os.path.isfile(dest_path):
                shutil.move(src_path,dest_path)

            elif os.path.isfile(dest_path) and \
                checkSum(src_path) == checkSum(dest_path):

                os.remove(src_path)
                print("removed" + src_path)

    return


def organize(path):

    fileTypes = {}
    fileTypes["Images"] = ["jpg","gif", "png","jpeg", "bmp"]
    fileTypes["Audio"] = ["mp3","wav","aiff","flac","aac"]
    fileTypes["Video"] = ["m4v","flv","mpeg","mov","mpg","mpe","wmv","MOV","mp4"]
    fileTypes["Documents"] = ["doc","docx","txt","ppt","pptx","pdf","rtf"]
    fileTypes["Executables"] = ["exe"]
    fileTypes["Compressed"] = ["zip","tar","rar"]
    fileTypes["Programming"] = ["c","cpp","java","py"]



    li = os.listdir(path)

    create_folders(path,fileTypes)


    for file in li:
        move_files(file,path,fileTypes)
