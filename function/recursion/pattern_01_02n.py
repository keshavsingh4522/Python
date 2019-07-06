def f(n,i):
 if n==0:
   return
 def g(t):
   if t==0:
     return
   g(t-1)
   print(t,end='')
 f(n-1,i+1)
 print(' '*(i-1),end="")
 g(n)
 print()
n=int(input('enter a number: '))
i=1
f(n,i)
'''
output:
enter a number: 6
     1
    12
   123
  1234
 12345
123456
'''
