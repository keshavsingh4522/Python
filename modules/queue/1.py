#1
import queue as q
q1=q.Queue()
for i in range(4):
    q1.put(int(input('enter number {} :'.format(i+1))))
while not q1.empty():
    print(q1.get())
'''
enter number 1 :12
enter number 2 :56
enter number 3 :78
enter number 4 :98
12
56
78
98
'''
#2
import queue as q
q1=q.LifoQueue()
for i in range(4):
    q1.put(int(input('enter number {} :'.format(i+1))))
while not q1.empty():
    print(q1.get())
'''
enter number 1 :12
enter number 2 :56
enter number 3 :22
enter number 4 :89
89
22
56
12
'''
#3
import queue as q
q1=q.PriorityQueue()
for i in range(4):
    q1.put(int(input('enter number {} :'.format(i+1))))
while not q1.empty():
    print(q1.get())
'''
enter number 1 :22
enter number 2 :56
enter number 3 :78
enter number 4 :111
22
56
78
111
'''
