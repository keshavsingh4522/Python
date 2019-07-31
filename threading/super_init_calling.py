import threading as th
import logging as lg
import time as t
lg.basicConfig(level=lg.DEBUG,format="%(threadName)-10s %(message)10s")
class mythread(th.Thread):
    def __init__(self,arg,target,kwargs):
        super().__init__(target=target)
        self.target=target
        self.args=arg
        self.kwargs=kwargs
    def run(self):
        self.target()
        lg.debug('running with %s and %s'%(self.args,self.kwargs))
def f():
    lg.debug('you are in function f')
if __name__=="__main__":
    t1=mythread(target=f,arg=(4,),kwargs={'a':'A','b':'B'})
    t1.start()
    t1.join()
'''
output:
Thread-1   you are in function f
Thread-1   running with (4,) and {'a': 'A', 'b': 'B'}
'''
