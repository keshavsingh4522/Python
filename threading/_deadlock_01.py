import time
import threading as th
lock=th.Lock()
x=0
def A():
    global x
    lock.acquire()
    for i in range(5):
        time.sleep(0.4)
        x-=1
        print('A x(x-=1):',x)
    lock.release()
def B():
    global x
    lock.acquire()
    for i in range(5):
        time.sleep(0.4)
        x+=4
        print('B x(x+=4)',x)
    lock.release()
def C():
    global x
    lock.acquire()
    for i in range(5):
        time.sleep(0.4)
        x-=5
        print('C x(x-=5)',x)
    lock.release()
def D():
    global x
    lock.acquire()
    for i in range(5):
        time.sleep(0.4)
        x+=3
        print('D x+=3',x)
    lock.release()
print('initially x: ',x)
t1=time.time()
l=[A,B,C,D]
l1=[]
for i in l:
    l1.append(th.Thread(target=i))
    l1[-1].start()
for i in l1:
    i.join()
t2=time.time()
print('you successfully executed programm')
print(t2-t1)
print('x: ',x)
'''
output:
initially x:  0
A x(x-=1): -1
A x(x-=1): -2
A x(x-=1): -3
A x(x-=1): -4
A x(x-=1): -5
B x(x+=4) -1
B x(x+=4) 3
B x(x+=4) 7
B x(x+=4) 11
B x(x+=4) 15
C x(x-=5) 10
C x(x-=5) 5
C x(x-=5) 0
C x(x-=5) -5
C x(x-=5) -10
D x+=3 -7
D x+=3 -4
D x+=3 -1
D x+=3 2
D x+=3 5
you successfully executed programm
8.012572765350342
x:  5
'''
