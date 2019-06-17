n=int(input("enter a number: "))
i=1
while i<=n:
 j=i
 c=0
 k=j
 while j>0:
  print(k," ",sep='',end="")
  k=k+n-1-c
  j-=1
  c+=1
 i+=1
 print()
'''
output:
enter a number: 9
1 
2 10 
3 11 18 
4 12 19 25 
5 13 20 26 31 
6 14 21 27 32 36 
7 15 22 28 33 37 40 
8 16 23 29 34 38 41 43 
9 17 24 30 35 39 42 44 45
'''
