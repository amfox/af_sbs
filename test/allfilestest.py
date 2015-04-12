# coding=utf-8
import fnmatch
import os

__author__ = 'tif'


def all_files(root, patterns="*", single_level=False, yield_folders=False):
    patterns = patterns.split(";")
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
        if single_level:
            break


if __name__ == "__main__":
    import pdb

    pdb.set_trace()

    for a in all_files(root="F:"):
        print a