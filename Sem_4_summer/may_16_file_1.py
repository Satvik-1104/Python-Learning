# copying a file and moving a file
# copyfile() - copies contents of a fle
# copy() -     copyfile() + permission mode + destination can be a directory
# copy2() -    copy() + copies metadata (file's creation and modification times)

# import shutil
# shutil.copyfile("text.txt", "text2.txt")

# the source and destination can be file paths too

import os

source = "folder"
destination = "C:\\Users\\HP\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file at the destination with the same name")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found!")
