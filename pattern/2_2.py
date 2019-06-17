n=int(input("enter a number: "))
for i in range(1,n+1):
  print('*'*i,sep='')
for i in range(n-1,0,-1):
 print('*'*i,sep='')
 '''
 output:
 enter a number: 5
*
**
***
****
*****
****
***
**
*
 '''
