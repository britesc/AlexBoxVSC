"""
    File System Utilities.
"""
import uos
def dir_exists(filename):
    try:
        return (uos.stat(filename)[0] & 0x4000) != 0
    except OSError:
        return False
        
def file_exists(filename):
    try:
        return (uos.stat(filename)[0] & 0x4000) == 0
    except OSError:
        return False
