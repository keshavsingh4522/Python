import time
import threading as th
import logging as lg
lg.basicConfig(level=lg.DEBUG,format="%(threadName)-10s %(message)10s")
def f():
    print('hello','timer')
if __name__=='__main__':
    print('waiting for 5 seconds')
    t=th.Timer(5,f)#wait for 5 second
    t.start()
'''
output:
waiting for 5 seconds
hello timer
'''
