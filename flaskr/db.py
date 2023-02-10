import sqlite3
import pathlib
import glob
import os
import random

MASTER_DATABASE = "master.db"
APP_NAME = "flaskr"
PATH = "static/img/i_ver1"

def createImages():
    con = sqlite3.connect(MASTER_DATABASE)
    db_paths = con.execute("SELECT path FROM images").fetchall()
    paths = [item[0] for item in db_paths]

    extensions = ["png", "jpg", "jpeg", "webp", "gif", "jfif"]
    cur = pathlib.Path.joinpath(pathlib.Path(__file__).parent, PATH)
    allFIle = []

    for ext in extensions:
        allFIle.extend(getFiles(cur, ext))
    for file in allFIle:
        path = file.split(APP_NAME)[1]
        if (path not in paths):
            con.execute(f'INSERT INTO images(path, score, like) VALUES("{path}", "100", "0")')
    con.commit()
    con.close

def getFiles(path, extension):
    file_list = []
    for filename in glob.glob(os.path.join(path, f'*.{extension}')):
        file_list.append(filename)
    for dirname in glob.glob(os.path.join(path, '*')):
        if os.path.isdir(dirname):
            file_list.extend(getFiles(dirname, extension))
    return file_list
