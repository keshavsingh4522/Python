=int(input("enter a number: "))
i=1
while i<=n:
 print(' '*(n-i),sep='',end="")
 j=1
 while j<=i:
  print(j,sep='',end="")
  j+=1
 j=i-1
 while j>=1:
  print(j,sep='',end="")
  j-=1
 i+=1
 print()
'''
output:
enter a number: 6
     1
    121
   12321
  1234321
 123454321
12345654321
'''
