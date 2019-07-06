def f(n):
 if n==0:
  return
 def g(t):
   if t==0:
     return
   g(t-1)
   print(t,end=' ')
 g(n)
 print()
 f(n-1)
n=int(input('enter a number: '))
f(n)
'''
output:
enter a number: 6
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
