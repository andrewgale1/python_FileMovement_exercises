#Scenario: You you will have to provide for recording the last time the 'file check' process was performed,
#so that you can be sure to cover the entire time period in which new or edited files could occur.
#To do this, you will need to create a database with a table that can store the date and time of the last 'file
#check' process. That way, you can use that date/time as a reference point in terms of finding new or
#modified files. As part of this project, the users are asking that their UI display the date and time of the last 'file check'
#process. You have been asked to implement this functionality. This means that you will need to:
#- create a database and a table
#- modify your script to both record date/time of 'file check' runs and to retrieve that data for use in
#  the 'file check' process, and modify the UI to display the last 'file check' date/time

import tkinter
import _tkinter
from tkinter import *
from tkinter import ttk
import os
import shutil
import time
import fileCheck_and_fileMove_mod


class FileMover:

    def __init__(self, master):
        

        master.title('Move Your Modified Files')
        master.resizable(False,False)

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack(fill=BOTH)
        ttk.Label(self.frame_header,
                  text = ("Select source and destination folders. Then 'Move Files' that have been modified "
                          "since the last file move...")).pack(pady=15)                  
                                                 
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(fill=BOTH)

        ttk.Button(self.frame_content, text='Select Source Folder', command= lambda: self.getSource()).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Select Destination Folder', command= lambda: self.getDest()).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.frame_content, text='Move Files', command= (lambda: self.get_last_check())).grid(row=2, column=0, padx=10, pady=20)

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

        ttk.Label(self.frame_content, text="Last File Check").grid(row=2, column=1, padx=10, pady=3)
        self.last_check = StringVar()
        self.last_check.set(fileCheck_and_fileMove_mod.return_last())
        self.entry_dst = ttk.Entry(self.frame_content, width=60, textvariable=self.last_check)
        self.entry_dst.grid(row=2, column=2, padx=10, pady=3)
        self.entry_dst.configure(state='readonly')


    def get_last_check(self):
        fileCheck_and_fileMove_mod.moveModifiedFiles(self.src_var.get(),self.dst_var.get())
        self.last_check.set(fileCheck_and_fileMove_mod.return_last())       
    
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

