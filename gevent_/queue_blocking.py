# -*- coding:utf-8 -*-
import gevent
from gevent.queue import Queue, Empty

tasks = Queue(3)


def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1) # decrements queue size by 1
            print('Worker %s got task %s' % (n, task))
            gevent.sleep(0)
    except Empty:
        print 'Quitting time!'


def boss():
    for i in xrange(10):
        tasks.put(i)

    print 'Round 1 done!'

    for i in xrange(15):
        tasks.put(i)

    print 'Round 2 done!'



gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steven'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'sam')
])