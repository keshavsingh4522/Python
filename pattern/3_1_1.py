=int(input("enter a number: "))
for i in range(1,n+1):
 print(' '*(i-1),i,sep='',end="")
 print(' '*(2*(n-i)-1),i if i!=n else "",sep='')
#print(' '*(2*(n-i)-1),'*',sep='') if i!=n else print()
for i in range(n-1,0,-1):
 print(' '*(i-1),i,sep='',end="")
 print(' '*(2*(n-i)-1),i,sep='')
 '''
 output:
 enter a number: 6 
1         1
 2       2
  3     3
   4   4
    5 5
     6
    5 5
   4   4
  3     3
 2       2
1         1
 '''
