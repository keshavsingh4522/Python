class A:
 def __init__(self):
  print('class A',type(self))
class B(A):
 def __init__(self):
  super().__init__()
  print('class B',type(self))
class C(B):
 def __init__(self):
  super().__init__()
  print('class C',type(self))
c=C()
'''
output:
class A <class '__main__.C'>
class B <class '__main__.C'>
class C <class '__main__.C'>
'''
