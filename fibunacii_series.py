n=int(input("Enter a number: "))
a=0
b=1
if n>0:
  print("The following are",n,"number of elemnts in a fibonacci series")
for i in range(n):
  print(a,end=' ')
  t=a+b
  a=b
  b=t
'''
output:
enter a number: 15
0 	1 	1 	2 	3 	5 	8 	13 	21 	34 	55 	89 	144 	233 	377 	
'''
