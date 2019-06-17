n=int(input("enter a number: "))
for i in range(1,n+1):
 print(' '*(i-1),'*',sep='',end="")
 print(' '*(2*(n-i)-1),'*' if i!=n else "",sep='')
#print(' '*(2*(n-i)-1),'*',sep='') if i!=n else print()
for i in range(n-1,0,-1):
 print(' '*(i-1),'*',sep='',end="")
 print(' '*(2*(n-i)-1),'*',sep='')
 '''
 output:
 enter a number: 7
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *
     * *
    *   *
   *     *
  *       *
 *         *
*           *
 '''
