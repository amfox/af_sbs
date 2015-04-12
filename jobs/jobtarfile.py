# coding=utf-8
import os
from tarfile import TarFile

__author__ = 'TIF'


def my_filter(tarinfo):
    import pdb

    pdb.set_trace()
    # increment some count
    # add tarinfo.size to some byte counter
    return tarinfo


if __name__ == "__main__":

    tar = TarFile(name='aaaa.tar', mode='w')

    for root, dir, files in os.walk("E:\\test"):
        import pdb

        pdb.set_trace()
        for file in files:
            fullpath = os.path.join(root, file)
            tar.add(name=fullpath, filter=my_filter)
    tar.close()