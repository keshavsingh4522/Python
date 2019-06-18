n=int(input("enter a number: "))
for i in range(1,n+1):
  if i!=n:
   print("* ","  "*(n-2),'* '*n if i==1 else "* ",sep='',end="")
  else:
   print('* '*(2*n-1),end="",sep='')
  print()
for i in range(1,n):
 if i!=n-1:
  print('  '*(n-1),'* ','  '*(n-2),'* ',end='',sep="")
 else:
  print('* '*n,'  '*(n-2),'* ',end='',sep="")
 print()
 '''
 output:
 enter a number: 6
*         * * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * * * * * * * 
          *         * 
          *         * 
          *         * 
          *         * 
* * * * * *         * 
 '''
