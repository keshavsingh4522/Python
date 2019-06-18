n=int(input("enter a number: "))
for i in range(n,0,-1):
  for j in range(n,0,-1):
   if(j>i):
    print(j,' ',sep='',end="")
   else:
    print(i,' ',sep='',end="")
  print()
'''
output:
enter a number: 6
6 6 6 6 6 6 
6 5 5 5 5 5 
6 5 4 4 4 4 
6 5 4 3 3 3 
6 5 4 3 2 2 
6 5 4 3 2 1
'''
