n=int(input("enter number to convert in words: "))
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
d1=0
rev=0
while n:
  rev=rev*10+n%10
  n=n//10
  d1+=1
d2=0
while rev:
  print(d[rev%10],end=' ')
  rev=rev//10
  d2+=1
for i in range(d1-d2):
 print("zero",end=' ')
print()
'''
output:
enter number to convert in words: 20000
two zero zero zero zero
'''
