
import glob
import os
import random
import subprocess


def getRandom(n = 8):
    return random.randint(10**(n - 1), 10**n - 1)

def getFiles(path, extension):
    file_list = []
    for filename in glob.glob(os.path.join(path, f'*.{extension}')):
        file_list.append(filename)
    for dirname in glob.glob(os.path.join(path, '*')):
        if os.path.isdir(dirname):
            file_list.extend(getFiles(dirname, extension))
    return file_list

def openSubprocess(path):
    subprocess.Popen(['start', path], shell=True)
