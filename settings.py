# coding=utf-8
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

__author__ = 'TIF'

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///backupstore.sqlite'),
    'recoverstore': SQLAlchemyJobStore(url='sqlite:///recoverstore.sqlite')
}
executors = {
    'default': {'type': 'threadpool', 'max_workers': 1},
    'processpool': ProcessPoolExecutor(max_workers=1)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}