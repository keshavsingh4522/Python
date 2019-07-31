import threading as th
import logging as lg
lg.basicConfig(level=lg.DEBUG,format="%(threadName)10s %(message)-10s")
lg.debug('hello')
class keshav(th.Thread):
    def run(self):
        lg.debug('keshav')
t=keshav()
t.start()
t.join()
'''
output:
MainThread hello     
 Thread-17 keshav
'''
