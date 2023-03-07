import os
import shutil

path = input()


def automate(path=None):
    files = os.listdir(path)
    DIRECTORIES = {
        "HTML": [".html5", ".html", ".htm", ".xhtml"],
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                   ".heif", ".psd"],
        "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp"],
        "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      ".pptx",".csv"],
        "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"],
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
        "PLAINTEXT": [".txt", ".in", ".out"],
        "PDF": [".pdf"],
        "PYTHON": [".py"],
        "XML": [".xml"],
        "EXE": [".exe"],
        "SHELL": [".sh"],

    }
    FILE_FORMATS = {file_format: directory
                     for directory, file_formats in DIRECTORIES.items()
                     for file_format in file_formats}

    def GetKey(val):
        print(val)
        if val in FILE_FORMATS:
            return FILE_FORMATS[val]
        elif val == ".DOCUMENTS":
            return val
        else:
            return val



    if files != []:
        for f in files:

            splitted_file_name = f.split('.')
            extention = splitted_file_name[-1]
            # value = {i for i in DIRECTORIES if DIRECTORIES[i] == extention}
            print()
            if not os.path.exists(f"{path}/{FILE_FORMATS['.'+extention]}"):
                os.mkdir(f"{path}/{GetKey('.'+extention)}")
            if extention in f:
                src = f"{path}/{f}"
                dst = f"{path}/{GetKey('.'+extention)}"
                shutil.move(src,dst)

    else:
        return "empty"



automate(path)

# import os
#
# print('File name :    ', os.path.basename(__file__))
# print('Directory Name:     ', os.path.dirname(__file__))
