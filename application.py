# coding=utf-8
import os
import tornado
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_ADDED
from apscheduler.schedulers.tornado import TornadoScheduler
from handler.AddJobHandler import AddJobHandler
from handler.BackUIHandler import BackUIHandler
from handler.DebugHandler import DebugHandler
from handler.GetJobHandler import GetJobHandler
from handler.GetJobsHandler import GetJobsHandler
from handler.ModifyJobHandler import ModifyJobHandler
from handler.PauseJobHandler import PauseJobHandler
from handler.RemoveJobHandler import RemoveJobHandler
from handler.ResumeJobHandler import ResumeJobHandler
from handler.RunJobHandler import RunJobHandler
from settings import jobstores, executors, job_defaults


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", DebugHandler),
            (r"/backui", BackUIHandler),

            (r"/job/getjob", GetJobHandler),
            (r"/job/getjobs", GetJobsHandler),

            (r"/job/addjob", AddJobHandler),
            (r"/job/removejob", RemoveJobHandler),

            (r"/job/runjob", RunJobHandler),
            (r"/job/modifyjob", ModifyJobHandler),
            (r"/job/pausejob", PauseJobHandler),
            (r"/job/resumejob", ResumeJobHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Scheduler of jobs
        self.scheduler = TornadoScheduler()
        self.scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
        self.scheduler.add_listener(self.listener, EVENT_JOB_ADDED | EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    def listener(self, event):
        print "jobid:", event.job_id, "jobstore", event.jobstore, "eventcode:", event.code

