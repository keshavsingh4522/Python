class E:
 pass
class F:
 pass
class G:
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
class D(B):
 def __init__(self):
  super().__init__()
  print('class D')
class E(C):
 def __init__(self):
  super().__init__()
  print('class E')
class F(E,D):
 def __init__(self):
  super().__init__()
  print('class F')
class G(E):
 def __init__(self):
  super().__init__()
  print('class G')
class H(F,G):
 def __init__(self):
  super().__init__()
  print('class H')
h=H()
'''
output:

'''
