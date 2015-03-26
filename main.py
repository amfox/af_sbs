# coding=utf-8
import os
import tornado
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from application import Application

__author__ = 'TIF'

define("port", default=5000, help="run on the given port", type=int)

if __name__ == "__main__":
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        application = Application()
        application.scheduler.start()
        http_server = HTTPServer(application)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass