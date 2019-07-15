class Indexer:
 def __init__(self):
  pass
 def __getitem__(self,index):
  return index**2
obj=Indexer()
print(obj[4])
'''
output:
16
'''
