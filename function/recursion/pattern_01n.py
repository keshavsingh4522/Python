def f(n):
 if n==0:
  return
 def g(t):
   if t==0:
     return
   g(t-1)
   print(t,end=' ')
 f(n-1)
 g(n)
 print()
n=int(input('enter a number: '))
f(n)
'''
output:
enter a number: 7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7
'''
