class Indexer:
 def __init__(self,r,i):
  self.real=r
  self.imag=i
 def __iadd__(self,c):
  return Indexer(self.real+c.real,self.imag+c.imag)
 def __str__(self): #repr or str
  return '{} i{}'.format(self.real,self.imag)
c1=Indexer(10,20)
c2=Indexer(40,80)
print('c1 : ',c1)
print('c2 : ',c2)

c1+=c2

print('c3 : ',c1)
'''
output:
c1 :  10 i20
c2 :  40 i80
c3 :  50 i100
'''
