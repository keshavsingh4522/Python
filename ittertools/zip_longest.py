>>> import itertools as it
>>>'''1.problem'''
...
>>> l1=[1,2,3,4,5,67]
>>> l2=[8,6,5,4]
>>> list(zip(l1,l2))
[(1, 8), (2, 6), (3, 5), (4, 4)
>>>
>>> '''1.solution'''
...
>>> list(it.zip_longest(l1,l2))
[(1, 8), (2, 6), (3, 5), (4, 4), (5, None), (67, None)]
>>>
>>>
>>>
>>> '''2.problem'''
...
>>> l1=[1,2,3,4,5]
>>> t1=5,4,3,2,1
>>> s1='hello'
>>> l1+t1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "tuple") to list
>>>
>>>'''2.solution'''
...
>>> list(it.chain(l1,t1))
[1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
>>> list(it.chain(l1,t1,s1))
[1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 'h', 'e', 'l', 'l', 'o']
>>> list(it.chain(l1,t1,s1,'keshav singh'))
[1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 'h', 'e', 'l', 'l', 'o', 'k', 'e', 's', 'h', 'a', 'v', ' ', 's', 'i', 'n', 'g', 'h']
