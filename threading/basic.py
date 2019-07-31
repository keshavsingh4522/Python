import threading as th
lock=th.Lock()
x=0
def a():
    global x
    for i in range(10000):
        x-=2
    print(x)
def b():
    global x
    for i in range(10000):
        x+=2
    print(x)
def c():
    global x
    for i in range(10000):
        x-=3
    print(x)
def d():
    global x
    for i in range(10000):
        x+=3
    print(x)
l=[a,b,c,d]
for i in l:
    t=th.Thread(target=i)
    t.start()
print(x)
'''
output:
-20000
0-30000

00
'''
