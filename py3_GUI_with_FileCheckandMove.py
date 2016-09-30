#Scenario: You recently created a script that will check a folder for new or modified files,
#and then copy those new or modified files to another location.
#Users are asking for a user interface to make using the script easier and more versatile.
#Desired features of the UI:
#-Allow the user to browse to and choose a specific folder that will contain the
#files to be checked daily.
#-Allow the user to browse to and choose a specific folder that will receive the
#copied files.
#-Allow the user to manually initiate the 'file check' process that is performed by
#the script.
#You have been asked to create this UI. Use Python 3.4 and tkinter to create the UI.

import tkinter
import _tkinter
from tkinter import *
from tkinter import ttk
import os
import shutil
import time
import python_fileCheck_and_fileMove_mod


class FileMover:

    def __init__(self, master):
        

        master.title('Move Your Modified Files')
        master.resizable(False,False)

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack(fill=BOTH)
        ttk.Label(self.frame_header,
                  text = ("Select source and destination folders. Then 'Move Files' that have been modified "
                          "in the last 24 hours.")).pack(pady=15)                  
                                                 
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(fill=BOTH)

        ttk.Button(self.frame_content, text='Select Source Folder', command= lambda: self.getSource()).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Select Destination Folder', command= lambda: self.getDest()).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Move Files', command= lambda: python_fileCheck_and_fileMove_mod.moveModifiedFiles(self.src_var.get(),self.dst_var.get())).grid(row=2, column=0, padx=10, pady=20)

        ttk.Label(self.frame_content, text="Source Folder").grid(row=0, column=1, padx=10, pady=3)
        self.src_var = StringVar()
        self.entry_src = ttk.Entry(self.frame_content, width=60, textvariable=self.src_var)
        self.entry_src.grid(row=0, column=2, padx=10, pady=3)
        self.entry_src.configure(state='readonly')
        
        ttk.Label(self.frame_content, text="Destination Folder").grid(row=1, column=1, padx=10, pady=3)
        self.dst_var = StringVar()
        self.entry_dst = ttk.Entry(self.frame_content, width=60, textvariable=self.dst_var)
        self.entry_dst.grid(row=1, column=2, padx=10, pady=3)
        self.entry_dst.configure(state='readonly')


    def getSource(self):
        src_dirname = filedialog.askdirectory()
        self.src_var.set(src_dirname+'/')

    def getDest(self):
        dst_dirname = filedialog.askdirectory()
        self.dst_var.set(dst_dirname+'/')
  
 
def main():
    root = Tk()
    filemover = FileMover(root)
    root.mainloop()

if __name__ == "__main__": main()
