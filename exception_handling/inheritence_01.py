class father:
 def __init__(self):
  self.fage=int(input('enter father age: '))
  if self.fage<=0:
   raise ValueError('age must be grater then zero')
 def display(self):
  print('Father age is: ',self.fage)
class son(father):
 def __init__(self):
  super().__init__()
  self.sage=int(input('enter son age: '))
  if self.sage<=0:
   raise ValueError('age must be +ve')
  if self.sage>=self.fage:
   raise ValueError('son age must be less then father age')
 def display(self):
  print('son age is: ',self.sage)
while True:
 try:
  f=father()
 except Exception as e:
  print(e)
 else:
  f.display()
  break
while True:
 try:
  s=son()
 except Exception as e:
  print(e)
 else:
  s.display()
  break
'''
output:
enter father age: -9
age must be grater then zero
enter father age: 45
Father age is:  45
enter father age: 67
enter son age: -34
age must be +ve
enter father age: 98
enter son age: 101
son age must be less then father age
enter father age: 67
enter son age: 45
son age is:  45
'''
