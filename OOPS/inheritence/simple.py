class Parent:
 def __init__(self):
  self.__roll=1234 # __  -> it make private
  self.__name='keshav'
 def disp(self):
  print(self.__roll)
  print(self.__name)
p=Parent()
p.disp()
'''
output:
1234
keshav
'''
