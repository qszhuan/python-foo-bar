# -*- coding:utf-8 -*-
import time
import gevent
from gevent.select import select


start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)


def gr1():
    print '1. Started Polling: %s' % tic()
    select([], [], [], 2)
    print '3. Ended Polling: %s' % tic()


def gr2():
    print '2. Hey lets do some stuff while the greenlet poll, %s' % tic()
    gevent.sleep(1)


gevent.joinall([gevent.spawn(gr1),
                gevent.spawn(gr1),
                gevent.spawn(gr2)])