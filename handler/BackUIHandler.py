# coding=utf-8
from tornado.web import RequestHandler

__author__ = 'TIF'

# AnyCloud Win32service backup UI Handler. For gernerate the backup List
class BackUIHandler(RequestHandler):
    def get(self):
        # import  pdb
        # pdb.set_trace()
        # sc = self.application.scheduler
        # jobs = sc.get_jobs()
        # import pdb
        #
        # pdb.set_trace()
        # self.application.scheduler.triggers.cron.CronTrigger

        # job = self.application.scheduler.add_job(localbackup, 'interval', seconds=1)
        # self.application.scheduler.add_job(test, 'interval', next_run_time=None, args=('aa', 'bb'))
        self.render("base.html")
