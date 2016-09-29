#Scenario: Your employer wants a program to move all his .txt files from
#one folder to another On your desktop make 2 new folders. Call one Folder A &
#the second Folder B. Create 4 random .txt files & put them in Folder A.
#- Move the files from Folder A to Folder B.
#- Print out each file path that got moved onto the shell.
#- Upon viewing Folder A after the execution, the moved files should not be there.


import os
import shutil

def moveFiles(src, dst):
 
    file_list = os.listdir(src)
    for file_name in file_list:
        if file_name.endswith('.txt'):
            shutil.move(src+file_name, dst)
            print os.path.abspath(dst+file_name)

src = ("/Users/andrew/Desktop/Folder_A/")
dst = ("/Users/andrew/Desktop/Folder_B/")

moveFiles(src, dst)
