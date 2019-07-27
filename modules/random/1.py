import random as rd
for i in range(5):
    print(rd.rand(1,100))
'''
output:
36
53
48
85
19
'''
l=['keshav','keshav singh','priya jain','keshav dev','pari']
for i in l:
    print(rd.choices(l))
'''
ouyput:
['keshav dev']
['priya jain']
['keshav dev']
['pari']
['keshav']
'''
