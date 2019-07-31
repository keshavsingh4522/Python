import threading as th
import logging as lg
import time as t
lg.basicConfig(level=lg.DEBUG,format="%(threadName)-10s %(message)10s")
def f():
    lg.debug('starting f')
    t.sleep(3)
    lg.debug('ending f')
def h():
    lg.debug('starting h')
    t.sleep(1)
    lg.debug('ending h')
t1=th.Thread(target=f,daemon=True)
t2=th.Thread(target=h)
t1.start()
t2.start()
'''
output:
Thread-1   starting f
Thread-2   starting h
Thread-2     ending h
'''
