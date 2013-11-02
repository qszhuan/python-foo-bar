# -*- coding:utf-8 -*-
import gevent


def foo():
    print '1. Running in foo.'
    gevent.sleep(0)
    print '3. Explicit context switch back to foo again.'


def bar():
    print '2. Explicit context to bar'
    gevent.sleep(0)
    print '4. Explicit context switch back to bar'


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])

