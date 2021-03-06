# -*- coding:utf-8 -*-
import gevent
from gevent.queue import Queue


tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print 'Worker %s got task %s' % (n, task)
        gevent.sleep(0)

    print('Quitting time!')


def boss():
    for i in xrange(25):
        tasks.put_nowait(i)


gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'steven'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'sam')
])