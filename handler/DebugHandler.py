# coding=utf-8

from progressbar import ProgressBar, Counter, Timer
import time
from tornado.web import RequestHandler

__author__ = 'TIF'

def localbackup():
    widgets = ['Back Processed: ', Counter(), ' files (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(112))):
        # if i == int(filenum):
        # scheduler.remove_all_jobs()
        time.sleep(0.2)


class DebugHandler(RequestHandler):
    def get(self):
        sc = self.application.scheduler
        jobs = sc.get_jobs()
        import pdb

        pdb.set_trace()
        # self.application.scheduler.triggers.cron.CronTrigger

        # job = self.application.scheduler.add_job(localbackup, 'interval', seconds=1)
        # self.application.scheduler.add_job(test, 'interval', next_run_time=None, args=('aa', 'bb'))
        self.finish("Hello, world")
