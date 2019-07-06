>>>import ittertools as it
>>> l
[10, 2, 4, 5, 6, 34, 23, 1, 1, 11, 1, 23, 3, 33, 3]
>>> list(it.dropwhile(lambda x:x<11,l))
[34, 23, 1, 1, 11, 1, 23, 3, 33, 3]
>>> list(it.takewhile(lambda x:x<11,l))
[10, 2, 4, 5, 6]
>>> list(filter(lambda x:x<11,l))
[10, 2, 4, 5, 6, 1, 1, 1, 3, 3]
