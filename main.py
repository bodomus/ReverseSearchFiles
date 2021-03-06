import os
import re

import fileutils
from enum import Enum, unique

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


def compare2Directories(source, destination):
    """Проверить 2 директории. Если в source есть файлы которых нет в директории destination
    вывести эти фыайлы в первом столбце. Если во втором столбце есть файлы которых нет в первом столбце
    вывести эти файлы во втором столбце"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def write_strings(filename, dict):
    global total_original_files
    global total_dublicat_files
    file_object = open(filename, 'a+')
    file_object.write(f'total count original files: {total_original_files} \n')
    file_object.write(f'total count duplicate files: {total_dublicat_files} \n')
    sumlambda = lambda item, total: item + total
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


def prepare_files(base_dir1, base_dir2, dict_key):
    """ Сравниваем файлы из base_dir1 с base_dir2
    файл равен если хеш сумма одинакова или наименование и размер одинаков
    Extend `base_dir1`.  Class attribute `instances` keeps track
    of the number of `Keeper` objects instantiated.
    """
    if '' == base_dir1 or base_dir2 == '':
        raise ("Error base_dir1 or base_dir2 is empty")
    sdict = {}
    ddict = {}

    sdict = fileutils.create_dict(fileDir=base_dir1, dict_key=fileutils.Dict_key.FILE_NAME)
    ddict = fileutils.create_dict(fileDir=base_dir2, dict_key=fileutils.Dict_key.FILE_NAME)

    for skey in sdict.keys():
        svalue = sdict.get(skey)
        if svalue is not None:
            dkey = svalue['file_path'] if dict_key == fileutils.Dict_key.FILE_PATH else svalue['file_name']
            dvalue = ddict.get(dkey)
            if dvalue is not None:
                result_compare = compare_2files(svalue["file_path"], dvalue["file_path"])
                print_compare_result(svalue["file_path"], dvalue["file_path"], result_compare)


def print_compare_result(file1: object, file2: object, operation_result: bool) -> None:
    s1 = "файлы равны" if operation_result else "файлы не равны"
    print(f"{s1} \t Исходный файл \t Сравиваемый файл\n")
    print(f"Полный путь:{file1['file_path']} {file2['file_path']}  \n ")
    print(f"Имя файла:{file1['file_name']} {file2['file_name']}  \n ")
    print(f"Размер файла:{file1['file_size']} {file2['file_size']}  \n ")
    print(f"hash sum:{file1['file_hash']} {file2['file_hash']} ", end=f"\n{'-' * 80}\n")


def compare_2files(file1: object, file2: object) -> bool:
    """
    filename: file name
    filepath: full path with name
    size: size of file in bytes
    hash: hashfile
    сравниваем файлы Условия сравнения на равенство имена файлов равны, размер одинаков и хэш суммы совпадают
    :param file1: #dict с объектом
    :param file2: #dict с объектом
    :return: bool
    :Date: 2022-06-23
    :Version: 1
    :Authors:
        bodomus@gmail.com
    """
    result = False
    if file1 is None or file2 is None:
        raise ("compare_2files: the input param is None")
    if(file1['file_name'] == file2['file_name']) and (file1['file_hash'] == file2['file_hash']) and (file1['file_size'] == file2['file_size']):
        result = True
    if result:
        print_compare_result(file1=file1, file2=file2, operation_result=True)
    else:
        print_compare_result(file1=file1, file2=file2, operation_result=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #TODO split code on parts. And call them by arg from command string

    print_hi('PyCharm')
    prepare_files(r"d:/Work/CodeBooks/", r"d:/Work/CodeBooks1/", dict_key=fileutils.Dict_key.FILE_NAME)
    fileutils.create_dict(fileDir=r"d:/Work/CodeBooks/")
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
                    # shutil.move(path_file, 'j:/' + 'VideoFromProjects/'+file)
                    # list.append(f'filename: {path_file}: {size}\n')
                    check_file(path_file)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    write_strings(output_filename, filedict)

    print_hi('PyCharm end')
    print_hi(filesize)
