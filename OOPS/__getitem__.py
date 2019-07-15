class A:
 def __init__(self):
  self.l=[1,2,3,4,5,6,7,8,9]
 def __getitem__(self,i):
  if isinstance(i,int):
    return self.l[i]
  else:
   print(i.start,i.stop,i.step)
   return self.l[i]
a=A()
#for i in a.l:
# print(i,end='\t')
print(a[4])

print(a[:])
print(a[2:])
print(a[:5])
print(a[3:8])
print(a[::2])
print(a[:4:3])
print(a[4::3])
print(a[2:9:2])
'''
output:
5
None None None
[1, 2, 3, 4, 5, 6, 7, 8, 9]
2 None None
[3, 4, 5, 6, 7, 8, 9]
None 5 None
[1, 2, 3, 4, 5]
3 8 None
[4, 5, 6, 7, 8]
None None 2
[1, 3, 5, 7, 9]
None 4 3
[1, 4]
4 None 3
[5, 8]
2 9 2
[3, 5, 7, 9]
'''
