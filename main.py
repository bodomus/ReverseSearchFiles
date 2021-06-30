# This is a sample Python script.

import glob
import os
import re
import shutil


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def write_strings(filename, array):
    file_object = open(filename, 'a+')
    for string in array:
        file_object.write(string)
        print(f'{string}')
    file_object.close()

def check_file(fullfilepath):
    sizefile = os.path.getsize(path_file)
    name = os.path.splitext(fullfilepath)[0]
    ext = os.path.splitext(fullfilepath)[1]
    index = name.rfind('-')
    if index > -1:
        bodyfilename = name[index+1:len(name)]
        dublicat = os.path.dirname(fullfilepath) + '/' + bodyfilename + ext
        print(f'Original file name: {fullfilepath} | Source: {dublicat}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # glob.glob('*.mp4')
    pathes = 'd:/projects/photo'
    output_filename = 'd:/projects/photo/existfile.log'
    list = []
    i = 0
    filesize = 0
    for root, dirs, files in os.walk(pathes):
        for file in files:
            if file.endswith(".mp4") or file.endswith(".jpg") or file.endswith(".cr2"):
                path_file = os.path.join(root, file)
                result = re.search(r'-', file)
                i = i + 1
                #print(path_file, i)
                if result != None:
                    size = os.path.getsize(path_file)
                    filesize += size
                    # shutil.move(path_file, 'j:/' + 'VideoFromProjects/'+file)
                    list.append(f'filename: {path_file}: {size}\n')
                    check_file(path_file)
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    # write_strings(output_filename, list)

    print_hi('PyCharm end')
    print_hi(filesize)
