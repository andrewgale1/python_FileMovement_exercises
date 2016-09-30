
import os
import shutil
import time
import datetime
import sqlite3


def enterDB():
    connection = sqlite3.connect('file_check.db')
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS DateTime(check_time DATE)")
    realTime = datetime.datetime.now()
    c.execute("INSERT INTO DateTime VALUES(?)",(realTime,))
    connection.commit()


def return_last():
    connection = sqlite3.connect('file_check.db')
    c = connection.cursor()
    last_check = c.execute("SELECT check_time FROM DateTime WHERE ROWID = (SELECT MAX(ROWID) FROM DateTime)")
    for row in c.fetchone():
        return (row)
    connection.close()


def moveModifiedFiles(src, dst):
    file_list = os.listdir(src)
    for file_name in file_list:
        modTime = os.path.getmtime(src+file_name)
        checkTime = time.time() - 86400
        if modTime >= checkTime:
            shutil.move(src+file_name, dst)
            print (file_name + " has been moved to: " + os.path.abspath(dst+file_name))
    enterDB()
