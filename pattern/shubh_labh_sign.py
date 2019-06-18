n=int(input("enter a number: "))
for i in range(1,n+1):
  if i!=n:
   print("* ",sep='',end="")
   print("  "*(n-2),sep="",end='')
   if i==1:
    print("* "*n,sep='',end="")
   else:
    print("* ",end="",sep='')
  else:
   print('* '*(2*n-1),end="",sep='')
  print()
for i in range(1,n):
 if i!=n-1:
  print('  '*(n-1),end='',sep="")
  print('* ',end='',sep="")
  print('  '*(n-2),end='',sep="")
  print('* ',end='',sep="")
 else:
  print('* '*n,end='',sep="")
  print('  '*(n-2),end='',sep="")
  print("* ",sep="",end='')
 print()
'''
output:
enter a number: 9
*               * * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
* * * * * * * * * * * * * * * * * 
                *               * 
                *               * 
                *               * 
                *               * 
                *               * 
                *               * 
                *               * 
* * * * * * * * *               * 
'''
