import time
import threading as th
import logging as lg
lg.basicConfig(level=lg.DEBUG,format="%(threadName)-10s %(message)10s")
lock=th.Lock()
x=0
def A():
    lg.debug('Starting A')
    time.sleep(1)
    lg.debug('ending A')

def B():
    lg.debug('Starting B')
    time.sleep(1)
    lg.debug('ending B')

def C():
    lg.debug('Starting C')
    time.sleep(1)
    lg.debug('ending C')

def D():
    lg.debug('Starting D')
    time.sleep(1)
    lg.debug('ending D')

print('initially x: ',x)
t1=time.time()
l=[A,B,C,D]
print('at the start of program num of thread: ',th.active_count())
for i in l:
    t=th.Timer(3,i)
    t.start()
print('after starting num of thread: ',th.active_count())
for t in th.enumerate():
    if t.getName() in ['SockThread','MainThread']:
        continue
    else:
        # t.cancel()
        t.join()
print('at the end of program num of thread: ',th.active_count())
'''
output:
initially x:  0
at the start of program num of thread:  1
after starting num of thread:  5
Thread-1   Starting A
Thread-2   Starting B
Thread-3   Starting C
Thread-4   Starting D
Thread-2     ending B
Thread-3     ending C
Thread-1     ending A
Thread-4     ending D
at the end of program num of thread:  1
'''
