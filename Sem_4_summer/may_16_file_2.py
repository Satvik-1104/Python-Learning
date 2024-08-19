# deleting a file
# os.remove cannot delete an empty directory, we need os.rmdir
# os.dir annot delete a directory containing files, we need shutil.rmtree (considered risky)

import os
import shutil

path = "folder"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print(path + " not found!")
except PermissionError:
    print("An empty directory cannot be deleted by this function")
except OSError:
    print("A directory containing files cannot be deleted by this function")
else:
    print(path + " deleted")