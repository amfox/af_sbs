# coding=utf-8
from PyQt4 import QtGui
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

QtGui.QDirModel
# Configure the ListCache for jobprogress


# Configure the apscheduler jobstore & executor & job_defaults

# Default jobstore use sqlite3 for store the backup jobs
# Recover jobstore also use sqlite3 for store the recover jobs

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///backupstore.sqlite'),
    'recoverstore': SQLAlchemyJobStore(url='sqlite:///recoverstore.sqlite')
}

# All jobs will push into the threadpool to execute
executors = {
    'default': {'type': 'threadpool', 'max_workers': 1}
}

# Just allow one instance to run in the same time, it can be configed.
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

