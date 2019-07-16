
class Indexer:
 def __init__(self):
  self.l=[1,2,3,4,5,6,7,8,9]
 def __contains__(self,c):
  return c in self.l
c1=Indexer()
n=int(input('enter a number : '))
print(n in c1)
'''
output:
enter a number : 2
True
'''
