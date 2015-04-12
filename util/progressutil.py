# coding=utf-8
from progressbar import ProgressBar, FileTransferSpeed, Bar, Percentage, ETA, Counter, Timer
import time


def example2():
    class CrazyFileTransferSpeed(FileTransferSpeed):
        def update(self, pbar):
            return FileTransferSpeed.update(self, pbar)

    widgets = [CrazyFileTransferSpeed(), ' <<<', Bar(), '>>> ', Percentage(), ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000)
    pbar.start()
    for i in range(2000000):
        pbar.update(5 * i + 1)
    pbar.finish()


def example(filenum):
    widgets = ['Back Processed: ', Counter(), ' files (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(int(filenum) + 1))):
        time.sleep(0.1)


if __name__ == "__main__":
    example(11)