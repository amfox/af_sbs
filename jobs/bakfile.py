# coding=utf-8
import csv
import fnmatch
import hashlib
import os
import sys
import tarfile

__author__ = 'tif'


class BackFile(object):
    def __init__(self, jobid, files, folders, cache):
        self.jobid = jobid
        self.files = files
        self.folders = folders
        self.cache = cache

    def init_all_files(self):
        print "Read All Files ......"
        for folder in self.folders:
            for path in self.__get_folder_files(folder):
                self.files.append(path)
        return self.files

    def init_file_meta(self):
        print "Init Meta File ......"

        oldpath = os.getcwd()
        temppath = os.path.join(os.path.dirname(oldpath), 'temp')
        os.chdir(temppath)
        tempfile = "{0}.csv".format(self.jobid)
        csvfile = file(tempfile, 'wb')
        os.chdir(oldpath)

        temp = csv.writer(csvfile)
        for f in self.files:
            temp.writerow([self.__md5Checksum(f), os.path.getsize(f), os.path.getctime(f), f])
        csvfile.close()


    def back_all_files(self):
        oldpath = os.getcwd()
        temppath = os.path.join(os.path.dirname(oldpath), 'temp')
        for f in self.folders:
            print self.make_tar_folder(self.jobid, f, temppath)

    @classmethod
    def make_tar_folder(self, arcname, folder_to_backup, dest_folder, compression='gz'):
        if compression:
            dest_ext = "." + compression
        else:
            dest_ext = ""

        folder_name = os.path.basename(folder_to_backup)
        dest_name = "%s.tar%s" % (arcname, dest_ext)
        dest_path = os.path.join(dest_folder, dest_name)

        if compression:
            dest_cmp = ":" + compression
        else:
            dest_cmp = ""

        out = tarfile.TarFile.open(dest_path, 'w' + dest_cmp)
        out.add(folder_to_backup, folder_name)
        out.close()
        return dest_path

    @classmethod
    def __get_folder_files(self, root, patterns='*', single_level=False, yield_folders=False):
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

    @classmethod
    def __md5Checksum(self, filePath):
        fh = open(filePath, 'rb')
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        fh.close()
        return m.hexdigest()


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    bf = BackFile('ddd', [], ['F:\\temp', 'F:\\aa'], [])
    bf.init_all_files()
    bf.back_all_files()

    # os.path.exists(path)
    #
    # writer.writerow(bf.md5Checksum(path), os.path.getsize(path), os.path.getctime(path), path)