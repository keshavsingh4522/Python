n=int(input("Enter a number: "))
for i in range(1,n+1):
 print(" "*(n-i),"*"*(2*i-1),sep="")
 '''
 output:
 enter a number: 5
    *
   ***
  *****
 *******
*********
 '''
