n=int(input("enter a number: "))
a=0
b=1
for i in range(n):
  print(a,'\t',end='')
  t=a+b
  a=b
  b=t
'''
output:
enter a number: 15
0 	1 	1 	2 	3 	5 	8 	13 	21 	34 	55 	89 	144 	233 	377 	
'''
