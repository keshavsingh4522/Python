n=int(input("enter no of rows: "))
i=1
sum=1
k=0
while i<=n:
 j=i
 if i%2==0:
  sum=sum+i-1
  k=sum
 else:
  sum=k+1
 while j>0:
  print(sum,' ',sep='',end="")
  if i%2==0:
    sum-=1
  else:
    sum+=1
  j-=1
 print()
 i+=1
'''
output:
enter no of rows: 10
1 
3 2 
4 5 6 
10 9 8 7 
11 12 13 14 15 
21 20 19 18 17 16 
22 23 24 25 26 27 28 
36 35 34 33 32 31 30 29 
37 38 39 40 41 42 43 44 45 
55 54 53 52 51 50 49 48 47 46
'''
