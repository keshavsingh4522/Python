def f(n):
 if n==0:
  return
 f(n-1)
 print('*'*n)
n=int(input('enter a number: '))
f(n)
'''
output:
enter a number: 5
*
**
***
****
*****
'''
