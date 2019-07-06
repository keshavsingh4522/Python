def f(n):
 if n==0:
  return
 print('* '*n)
 f(n-1)
n=int(input('enter a number: '))
f(n)
'''
output:
enter a number: 5
* * * * * 
* * * * 
* * * 
* * 
*
'''
