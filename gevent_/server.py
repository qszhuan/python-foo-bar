# -*- coding:utf-8 -*-
import datetime
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class MainHandler(RequestHandler):
    def get(self):
        self.write({'datetime': str(datetime.datetime.utcnow())})


application = Application([
    (r"/", MainHandler),
])


if __name__ == '__main__':
    application.listen(port=8888)
    IOLoop.instance().start()