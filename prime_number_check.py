n=int(input("enter a number to check prime or not:  "))
c=0
for i in range(2,n//2+1):
 if(n%i==0):
  c+=1
  print("not prime")
  break
if c>0:
 pass
else:
 print("prime")
'''
output:
enter a number to check prime or not:  7
prime
'''
