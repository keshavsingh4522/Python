n=int(input("enter a number: "))
for i in range(1,n+1):
  for j in range(1,i+1):
   print(n-j+1,sep='',end="")
  for j in  range(i+1,n+1):
   print(n-i+1,sep='',end="")
  for j in range(1,n+1-i):
   print(n-i+1,end='',sep="")
  c=0
  for j in range(n+1-i,n):
   print(n-i+2+c,sep="",end='')
   c+=1
  print()
'''
output:
enter a number: 5
555555555
544444445
543333345
543222345
543212345
'''
