n=int(input("enter a number: "))
for i in range(1,n+1):
  for j in range(1,i+1):
   print(n-j+1,sep='',end="")
  for j in  range(i+1,n+1):
   print(n-i+1,sep='',end="")
  print()
'''
output:
enter a number: 6
666666
655555
654444
654333
654322
654321
'''
