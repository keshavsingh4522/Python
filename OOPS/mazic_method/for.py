class Indexer:
 def __init__(self,s,e):
  self.start=s
  self.end=e
 def __iter__(self):
  return self
 def __next__(self):
  if self.start==self.end:
   raise StopIteration
  else:
   t=self.start
   self.start+=1
   return t
for i in Indexer(1,11):
 print(i,end='\t')
print()
'''
output:
1	2	3	4	5	6	7	8	9	10	
'''
