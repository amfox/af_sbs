# coding=utf-8
from datetime import datetime
from tornado.web import RequestHandler

__author__ = 'TIF'


def tick():
    print('Tick! The time is: %s' % datetime.now())


class IndexHandler(RequestHandler):
    def get(self):
        # self.application.scheduler.add_job(tick, 'interval', seconds=3)
        import pdb

        pdb.set_trace()
        self.write("Hello, world")
