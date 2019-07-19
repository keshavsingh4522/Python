class Person:
 def __init__(self,n):
  self.name=n
 def IsEmployee(self):
  return False
 def __str__(self):
  return self.name

class Employee(Person):
 def __init__(self,n,i):
  super().__init__(n)
  self.id=i
 def IsEmployee(self):
  return True
 def __str__(self):
  return Person.__str__(self) +'\t'+str(self.id)
p=Person('Keshav Singh')
print(p)
print(p.IsEmployee())
e=Employee('Keshav Dev',178)
print(e)
print(e.IsEmployee())
'''
output:
Keshav Singh
False
Keshav Dev	178
True
'''
