
import glob
import os
import random
import subprocess

import bs4
import requests

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

def requestImg(url):
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.content, 'html.parser')
    title = soup.find('title').text
    imgs = soup.find_all('img')

    imageSrcs = []
    for img in imgs:
        s = {}
        for attr in ["alt", "src", "data-src", "srcset"]:
            if not (img.get(attr) is None):
                s[attr] = img.get(attr)
        imageSrcs.append(s)
    return {
        "title": title,
        "src": imageSrcs,
    }