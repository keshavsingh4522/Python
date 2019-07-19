class E:
 pass
class A:
 def __init__(self):
  print('class A')
class B(A):
 def __init__(self):
  super().__init__()
  print('class B')
class C(A):
 def __init__(self):
  super().__init__()
  print('class C')
class D(E,B):
 def __init__(self):
  super().__init__()
  print('class D')
class E(C):
 def __init__(self):
  super().__init__()
  print('class E')
class F(D,E):
 def __init__(self):
  super().__init__()
  print('class F')
f=F()
'''
output:
class A
class C
class E
class B
class D
class F
'''
