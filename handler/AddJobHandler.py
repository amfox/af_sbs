# coding=utf-8
import time
import json
from progressbar import ProgressBar, Counter, Timer
from handler.BaseHandler import BaseHandler

__author__ = 'tif'


def testlocalbackup(a, b):
    test1 = a
    test2 = b

    for i in range(101):
        time.sleep(0.2)
        barlen = i / 2
        print '\r|' + '#' * barlen + '-' * (50 - barlen) + '|', str(i) + '%',


def localbackup(filenum, name):
    widgets = ['Back Processed: ', Counter(), ' files (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(int(filenum) + 1))):
        # if i == int(filenum):
        # scheduler.remove_all_jobs()
        time.sleep(0.1)


class AddJobHandler(BaseHandler):
    def post(self):

        """
        @:param jobname 任务标识名
        @:param typeflag 任务标识位 0表示即时任务,1表示定时任务
        @:param syncflag 同步标志位 0表示不同步,1表示同步

        @:param foldlist
        @:param filelist

        @:param f1 typeflag=1时有效 表示分钟 (0-59)               example:[1,2,3]
        @:param f2 typeflag=1时有效 表示小时 (0-23)               example:[1,2,3]
        @:param f3 typeflag=1时有效 表示一个周的天 (1-7)           example:[1,3,5]

        """
        # jobname = self.get_body_argument('jobname')
        # typeflag = self.get_body_argument('typeflag')
        # syncflag = self.get_body_argument("syncflag")
        #
        # foldlist = self.get_body_arguments("foldlist")
        # filelist = self.get_body_arguments("filelist")
        #
        # f1 = self.get_body_argument("f1")
        # f2 = self.get_body_argument("f2")
        # f3 = self.get_body_arguments("f3")
        print self.from_body_get_arguments()

        # print typeflag, syncflag, foldlist, filelist, f1, f2, f3

        # args
        # jobtype = self.get_argument('jobtype')
        # runtime = self.get_argument('runtime')
        # folderargs = self.get_arguments('folders')
        # fileargs = self.get_arguments('files')
        # rundate = datetime.now()

        # sched = self.getsched()

        # sched.add_job(self.test, 'date',kwargs={'a': ['text', 'vvv', 'ccc'], 'b': 'aa'}, jobstore='recoverstore')
        # job = sched.add_job(testlocalbackup, 'date', args=[1, 4], name='localback')
        # job = self.application.scheduler.add_job(localbackup, 'interval', seconds=1, next_run_time=None,
        # args=('111', 'null'), misfire_grace_time=1, coalesce=True)

        self.finish("OK")




