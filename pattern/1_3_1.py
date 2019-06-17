n=int(input("enter a number: "))
for i in range(1,n+1):
 print(" "*(n-i),'* '*i,sep='')
 '''
 output:
 enter a number: 7
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * *
 '''
