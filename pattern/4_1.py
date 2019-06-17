n=int(input("enter a number: "))
for i in range(1,n+1):
 print(' '*(n-i),'*',sep='',end="")
 print(' '*(2*(i-1)-1),'*' if i!=1 else "",sep='')
for i in range(n-1,0,-1):
 print(' '*(n-i),'*',sep='',end="")
 print(' '*(2*(i-1)-1),'*' if i!=1 else "",sep='')
'''
output:
enter a number: 7
      *
     * *
    *   *
   *     *
  *       *
 *         *
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *
'''
