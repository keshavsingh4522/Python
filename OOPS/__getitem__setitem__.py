class Indexer:
 def __init__(self):
  self.data=[1,2,3,4,5,6,7,8,9]
 def __getitem__(self,index):
  return  self.data[index]
 def __setitem__(self,index,value):
  self.data[index]=value
obj=Indexer()
print(obj[4])
obj[4]=100
print(obj[4])
for i in obj:
 print(i,end=" ")
print('\n',list(obj))
'''
output:
5
100
1 2 3 4 100 6 7 8 9 
 [1, 2, 3, 4, 100, 6, 7, 8, 9]
'''
