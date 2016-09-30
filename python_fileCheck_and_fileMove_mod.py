#You should create two folders; one to hold the files that get created or
#modified throughout the day, and another to receive the folders that your
#script determines should be copied over daily.
#To aid in your development efforts, you should create .txt files to add
#to the first folder, using Notepad or similar program. You should also
#copy some older text files in there if you like. You should use files
#that you can edit, so that you can control whether they are meant to be
#detected as 'modified in the last 24 hours' by your program.



import os
import shutil
import time


def moveModifiedFiles(src, dst):
    file_list = os.listdir(src)
    for file_name in file_list:
        modTime = os.path.getmtime(src+file_name)
        checkTime = time.time() - 86400
        if modTime >= checkTime:
            shutil.move(src+file_name, dst)
            print (file_name + " has been moved to: " + os.path.abspath(dst+file_name))
    if modTime < checkTime:
            print ("No other files have been modified in the last 24 hours.")
            
