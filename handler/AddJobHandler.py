# coding=utf-8
import time
from apscheduler.triggers import date
from datetime import datetime
from progressbar import ProgressBar, Counter, Timer
from tornado.web import RequestHandler

__author__ = 'tif'

def testlocalbackup(a, b):
        test1 = a
        test2 = b

        for i in range(101):
            time.sleep(0.2)
            barlen = i / 2
            print '\r|' + '#' * barlen + '-' * (50 - barlen) + '|', str(i) + '%',

def localbackup(filenum, name):
    widgets = ['Back Processed: ', Counter(), ' files (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(int(filenum) + 1))):
        # if i == int(filenum):
        # scheduler.remove_all_jobs()
        time.sleep(0.1)


class AddJobHandler(RequestHandler):
    def getsched(self):
        return self.application.scheduler

    def get(self):
        # args
        # jobtype = self.get_argument('jobtype')
        # runtime = self.get_argument('runtime')
        # folderargs = self.get_arguments('folders')
        # fileargs = self.get_arguments('files')
        # rundate = datetime.now()

        sched = self.getsched()

        # sched.add_job(self.test, 'date',kwargs={'a': ['text', 'vvv', 'ccc'], 'b': 'aa'}, jobstore='recoverstore')
        job = sched.add_job(testlocalbackup, 'date', args=[1,  4], name='localback')
        # job = self.application.scheduler.add_job(localbackup, 'interval', seconds=1, next_run_time=None,
        # args=('111', 'null'), misfire_grace_time=1, coalesce=True)

        self.finish("OK")




