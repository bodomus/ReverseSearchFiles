import os
import enum
from pathlib import Path
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


def get_file_size_in_bytes(file_path):
    """ Get size of file at given path in bytes"""
    size = os.path.getsize(file_path)
    return size


def get_file_size_in_bytes_2(file_path):
    """ Get size of file at given path in bytes"""
    # get statistics of the file
    stat_info = os.stat(file_path)
    # get size of file in bytes
    size = stat_info.st_size
    return size


def get_file_size_in_bytes_3(file_path):
    """ Get size of file at given path in bytes"""
    # get file object
    file_obj = Path(file_path)
    # Get file size from stat object of file
    size = file_obj.stat().st_size
    return size


# Enum for size units
class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == SIZE_UNIT.KB:
        return size_in_bytes / 1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes / (1024 * 1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes / (1024 * 1024 * 1024)
    else:
        return size_in_bytes


def get_file_size(file_name, size_type=SIZE_UNIT.BYTES):
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.path.getsize(file_name)
    return convert_unit(size, size_type)


def get_hash(filename):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                return 0
            md5.update(data)
            sha1.update(data)

    print("MD5: {0}".format(md5.hexdigest()))
    print("SHA1: {0}".format(sha1.hexdigest()))
    return md5.hexdigest()


def create_dict(fileDir):
    """Создаем dict из директории. key нименование файла
     value dict с объектом
     filename: full path with name
     size: size of file in bytes
     hash: hashfile
     полный путь ?"""
    dir = {}
    file_item = {}
    for root, dirs, files in os.walk(fileDir):
        for file in files:
            statinfo = os.stat(file)
            file_item['file_size'] = statinfo.st_size
            file_item['file_name'] = os.path.join(root, file)
            file_item['file_hash'] = get_hash(os.path.join(root, file))

            print('file_size: %d' % statinfo.st_size)
            path_file = os.path.join(root, file)
            size = os.path.getsize(path_file)
            name = os.path.basename(path_file)

            #dir["file"] = file_item

            value = dir.get(path_file)nmjkoplkjiopl;123456tuiu8980














            if value is not None:
                dir.update({key: [f'{path_file}']})
            else:
                dir[key].append(f'{path_file}')

    return dir
