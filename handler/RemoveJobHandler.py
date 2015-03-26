# coding=utf-8
import json
from tornado.web import RequestHandler

__author__ = 'tif'


class RemoveJobHandler(RequestHandler):
    def get(self):
        jobid = self.get_argument('jobid')
        try:
            self.application.scheduler.remove_job(job_id=jobid)
        except:
            pass
        self.finish("OK")
