import logging as lg
import threading as th
import time as t
lg.basicConfig(level=lg.DEBUG,format="%(threadName)10s %(message)-10s")
def f():
    t.sleep(1)
    lg.debug('hello')
def g():
    t.sleep(1)
    lg.debug('keshav')
t1=th.Timer(1,f)
t2=th.Timer(1,g)
# t2=th.Timer(2,g)
t1.start()
t2.start()
t1.join()
t2.cancel()
'''
output:
Thread-55 hello   
Thread-56 keshav
'''
#
'''
output:
Thread-55 hello   
'''
