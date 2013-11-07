# -*- coding:utf-8 -*-
#
from datetime import datetime
import json
import urllib2
import gevent
import gevent.monkey
gevent.monkey.patch_socket()


def fetch(pid):
    print 'Process %s: start at %s' % (pid, str(datetime.utcnow()))
    response = urllib2.urlopen('http://localhost:8888')
    result = response.read()
    json_result = json.loads(result)
    date_time = json_result['datetime']
    print 'Process %s: %s' % (pid, date_time)


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    gevent.joinall([gevent.spawn(fetch, i) for i in range(1, 10)])


print 'Synchronous:'
synchronous()

print 'Asynchronous:'
asynchronous()