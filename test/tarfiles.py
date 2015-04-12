# coding=utf-8
import csv
import fnmatch
import hashlib
import os
import tarfile
import sys

__author__ = 'TIF'

# class TarFile(tarfile.TarFile):



def all_files(root, patterns='*', single_level=False, yield_folders=False):
    root = unicode(root, "utf8")
    patterns = patterns.split(';')
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


def md5Checksum(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    fh.close()
    return m.hexdigest()


def make_tar(folder_to_backup, dest_folder, compression='bz2'):
    if compression:
        dest_ext = '.' + compression
    else:
        dest_ext = ''

    arcname = os.path.basename(folder_to_backup)
    dest_name = '%s.tar%s' % (arcname, dest_ext)

    dest_path = os.path.join(dest_folder, dest_name)
    if compression:
        dest_cmp = ':' + compression
    else:
        dest_cmp = ''
    out = tarfile.TarFile.open(dest_path, 'w' + dest_cmp)
    out.add(folder_to_backup, arcname)
    import pdb;

    pdb.set_trace()
    out.extract()
    out.close()
    return dest_path


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    writer = csv.writer(file('aaaa.csv', 'wb'))

    for path in all_files('F:\\temp'):
        # print md5Checksum(path), path
        os.path.exists(path)
        import pdb
        pdb.set_trace()
        import win32api
        # win32api.GetFileAttributes(path)
        # win32api.GetFileVersionInfo()
        # win32api.FindFiles()
        print md5Checksum(path), os.path.getsize(path), os.path.getctime(path), path

        writer.writerow([md5Checksum(path), os.path.getsize(path), os.path.getctime(path), path])
        # make_tar('F:\\temp', 'F:\\', compression='gz')