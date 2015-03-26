from progressbar import ProgressBar, Counter, Timer
import time

__author__ = 'tif'


class LocalBackup:
    def __init__(self, jobid, folderargs=[], fileargs=[]):
        self.jobid = jobid
        self.folderargs = folderargs
        self.fileargs = fileargs
        self.initialize(self.jobid)

    def initialize(self, jobid):
        import pdb

        pdb.set_trace()
        pass

    def runback(self):
        pass

    def pauseback(self):
        pass

    def resumeback(self):
        pass

    def removeback(self):
        pass


def localbackup(filenum):
    widgets = ['Back Processed: ', Counter(), ' files (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(int(filenum) + 1))):
        time.sleep(0.1)


if __name__ == "__main__":
    lb = LocalBackup('aaaa', [], [])