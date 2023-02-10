
import glob
import os


def getFiles(path, extension):
    file_list = []
    for filename in glob.glob(os.path.join(path, f'*.{extension}')):
        file_list.append(filename)
    for dirname in glob.glob(os.path.join(path, '*')):
        if os.path.isdir(dirname):
            file_list.extend(getFiles(dirname, extension))
    return file_list