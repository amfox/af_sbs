# coding=utf-8
import json
from tornado.web import RequestHandler

__author__ = 'tif'


class GetJobsHandler(RequestHandler):
    def get(self):
        import pdb

        pdb.set_trace()
        jobid = self.get_argument('jobid')
        job = self.application.scheduler.get_job(job_id=jobid)

        data = {'id': job.id, 'args': (job.args if list(job.args) else []), 'name': job.name,
                'next_run_time': (job.next_run_time if job.next_run_time else 0)}
        self.finish(json.dumps(data))
