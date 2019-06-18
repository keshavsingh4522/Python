n=int(input('enter a number: '))
j=1
for i in range(1,n+1):
 print('*',sep='',end="")
 if i<(n//2+1):
  print('  '*(n//2-i+2),sep='',end="")
  print('* ',sep='',end="")
 else:
  print('  '*j,sep='',end="")
  print('* ',sep='',end="")
  j+=1
 print()
'''
output:
enter a number: 9
*          * 
*        * 
*      * 
*    * 
*  * 
*    * 
*      * 
*        * 
*          *
'''
