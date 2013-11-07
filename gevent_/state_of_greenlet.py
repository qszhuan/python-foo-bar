# -*- coding:utf-8 -*-
import gevent


def win():
    return 'You win!'


def fail():
    raise Exception('You failed!')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print 'Started?'
print winner.started
print loser.started

try:
    gevent.joinall([winner, loser])
except Exception as e:
    print 'This will never be reached.'

print 'Value?'
print winner.value
print loser.value

print 'Ready?'
print winner.ready()
print loser.ready()

print 'Successful?'
print winner.successful()
print loser.successful()

print 'Exception?'
print winner.exception
print loser.exception