import os
import enum
from pathlib import Path


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
