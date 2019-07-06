def f(n,i):
 if n==0:
   return
 def g(t):
   if t==0:
     return
   g(t-1)
   print(t,end='')
 def g2(t):
   if t==1:
      return
   print(t-1,end='')
   g2(t-1)
 f(n-1,i+1)
 print(' '*i,end="")
 g(n)
 g2(n)
 print()
n=int(input('enter a number: '))
i=0
f(n,i)
'''
enter a number: 6
     1
    121
   12321
  1234321
 123454321
12345654321
'''
