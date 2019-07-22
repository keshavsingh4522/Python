n=int(input('enter a number'))
for i in range(1,n+1):
 for j in range(0,n+1-i):
  if i<=(n//2+n%2):
   print(i%(n//2+n%2+1),end='')
  else:
   if n%2!=0:
    print(n//2+n%2-i%(n//2+n%2),end='')
   else:
    print(n//2-i%(n//2+1),end='')
 print()
'''
output:
enter a number8
11111111
2222222
333333
44444
4444
333
22
1
'''
'''
output:
111111111
22222222
3333333
444444
55555
4444
333
22
1
'''
