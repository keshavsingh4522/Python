n=int(input("enter a number: "))
for i in range(n,0,-1):
  for j in range(n,0,-1):
   if i>j:
    print(i,' ',sep='',end="")
   else:
    print(j,' ',sep='',end="")
  for j in range(2,n+1):
    if i>j:
      print(i,' ',end='',sep="")
    else:
      print(j,' ',end='',sep="")
  print()
for i in range(2,n+1):
  for j in range(n,0,-1):
   if i>j:
    print(i,' ',sep='',end="")
   else:
    print(j,' ',sep='',end="")
  for j in range(2,n+1):
    if i>j:
      print(i,' ',end='',sep="")
    else:
      print(j,' ',end='',sep="")
  print()
 '''
 output:
 enter a number: 7
7 7 7 7 7 7 7 7 7 7 7 7 7 
7 6 6 6 6 6 6 6 6 6 6 6 7 
7 6 5 5 5 5 5 5 5 5 5 6 7 
7 6 5 4 4 4 4 4 4 4 5 6 7 
7 6 5 4 3 3 3 3 3 4 5 6 7 
7 6 5 4 3 2 2 2 3 4 5 6 7 
7 6 5 4 3 2 1 2 3 4 5 6 7 
7 6 5 4 3 2 2 2 3 4 5 6 7 
7 6 5 4 3 3 3 3 3 4 5 6 7 
7 6 5 4 4 4 4 4 4 4 5 6 7 
7 6 5 5 5 5 5 5 5 5 5 6 7 
7 6 6 6 6 6 6 6 6 6 6 6 7 
7 7 7 7 7 7 7 7 7 7 7 7 7
 '''
