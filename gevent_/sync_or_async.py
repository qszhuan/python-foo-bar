# -*- coding:utf-8 -*-
import random
import timeit
import gevent


def task(pid):
    gevent.sleep(random.randint(0, 2) * 0.01)
    print 'Task %s done' % pid


def synchronous():
    for i in xrange(1, 10):
        task(i)


def asynchronous():
    gevent.joinall([gevent.spawn(task, i) for i in xrange(1, 10)])


if __name__ == '__main__':
    print 'Synchronous:'
    print timeit.timeit('synchronous()', 'from __main__ import synchronous', number=1)

    print 'Asynchronous:'
    print timeit.timeit('asynchronous()', 'from __main__ import asynchronous', number=1)

