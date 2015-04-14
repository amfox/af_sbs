import json
from tornado.web import RequestHandler


__author__ = 'TIF'


class BaseHandler(RequestHandler):
    @property
    def sched(self):
        return self.application.scheduler

    def from_body_get_arguments(self):
        body = self.request.body
        return json.load(body)