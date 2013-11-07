# -*- coding:utf-8 -*-
from gevent import Greenlet
import gevent


class MyGreenlet(Greenlet):
    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


g = MyGreenlet('Hi there!', 1)
g.start()
g.join()

gg = MyGreenlet.spawn('hello', 1)
gg.join()


