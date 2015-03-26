# coding=utf-8
from tornado.web import RequestHandler

__author__ = 'TIF'


class GetAllJobsHandler(RequestHandler):
    def get(self):
        # return self.application.scheduler.
        import pdb

        pdb.set_trace()