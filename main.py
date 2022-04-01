
import os
import re

import fileutils

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Поиск дублирующих файлов, которые отличаются только суффиксами  20200209_163926.jpg = 20200209_163926-2.jpg
###
pathes = 'd:/projects/photo/'
output_filename = 'd:/projects/photo/existfile.log'
list = []
dublicate_dict = {}

###
# Dictionary for result found files
filedict = {}
# Total original files
total_original_files = 0
# Total dublicat files
total_dublicat_files = 0
# Total size original files
total_size_original_files = {}
# Total size dublicate files
total_size_dublicate_files = 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




def write_strings(filename, dict):
    global total_original_files
    global total_dublicat_files
    file_object = open(filename, 'a+')
    file_object.write(f'total count original files: {total_original_files} \n')
    file_object.write(f'total count duplicate files: {total_dublicat_files} \n')
    sumlambda = lambda item, total : item + total
    sum = 0
    for i in total_size_original_files.values():
        sum += i

    file_object.write(f'total size original files: {sum} [{fileutils.convert_unit(sum, fileutils.SIZE_UNIT.MB)} MB]\n')
    file_object.write(
        f'total size dublicate files: {total_size_dublicate_files}  [{fileutils.convert_unit(total_size_dublicate_files, fileutils.SIZE_UNIT.MB)}] MB \n\n\n')
    for obj in dict.keys():
        value = dict.get(obj)
        if value is not None:
            file_object.write(f'Original file: {obj} \n')
            for f in value:
                file_object.write(f'\t {f} \n')

    get_dublicate_files(dict)
    file_object.write(f'++++++++++duplicate+++++++++++  \n')
    for value in dublicate_dict.values():
        if value is not None:
            file_object.write(f'\t {value} \n')
    file_object.close()


def get_dublicate_files(dict):
    for obj in dict.keys():
        value = dict.get(obj)
        if value is not None:
            for f in value:
                dublicate_dict.update({f: f})


def check_file(fullfilepath):
    """ Проверить файл на существование исходного файла без символа "-" с таким же свойствами"""
    global total_size_original_files
    global total_size_dublicate_files
    global total_original_files
    global total_dublicat_files

    sizefileodublicat = os.path.getsize(path_file)
    total_size_dublicate_files += sizefileodublicat
    dublicatname = os.path.basename(fullfilepath)
    ext = os.path.splitext(dublicatname)[1]
    filename = os.path.splitext(dublicatname)[0]
    index = filename.rfind('-')
    if index > -1:
        originalbodyfilename = filename[0:index]
        originalfilepath = os.path.dirname(fullfilepath) + '/' + originalbodyfilename + ext
        sizeoriginal = os.path.getsize(originalfilepath)
        key = f'{originalfilepath}#{sizeoriginal}'
        ovalue = total_size_original_files.get(key)
        if ovalue is None:
            total_size_original_files[key] = sizeoriginal

        if sizeoriginal == sizefileodublicat:
            print(
                f'Original file name: {originalfilepath} | Dublicat file name: {dublicatname}  Original file size: {sizeoriginal} | Dublicat file size: {sizefileodublicat}')

            value = filedict.get(key)

            if value is not None:
                filedict[key].append(f'{fullfilepath}')
                total_dublicat_files += 1
            else:
                filedict.update({key: [f'{fullfilepath}']})
                total_original_files += 1
                total_dublicat_files += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # glob.glob('*.mp4')

    i = 0
    filesize = 0
    for root, dirs, files in os.walk(pathes):
        for file in files:
            if file.endswith(".mp4") or file.endswith(".jpg") or file.endswith(".cr2"):
                path_file = os.path.join(root, file)
                result = re.search(r'-\d+', file)
                i = i + 1
                # print(path_file, i)
                if result != None:
                    size = os.path.getsize(path_file)
                    filesize += size
                    #shutil.move(path_file, 'j:/' + 'VideoFromProjects/'+file)
                    # list.append(f'filename: {path_file}: {size}\n')
                    check_file(path_file)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    write_strings(output_filename, filedict)

    print_hi('PyCharm end')
    print_hi(filesize)
