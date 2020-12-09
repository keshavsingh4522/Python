#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=[[i for i in range(1,n+1)] for i in range(n)]
        k=n
        for i in range(n//2):
            if n>1:
                # diagonal 4*(k-1)
                if i==0:
                    l[i+1][i]=4*(k-1)
                else:
                    l[i+1][i]=l[i][i-1]+4*(k-1)
                    # top left-right
                    for j in range(i,n-i):
                        l[i][j]=l[i][j-1]+1
                    # left top-bottom
                    for j in range(i+1,n-i+1):
                        l[j][i-1]=l[j-1][i-1]-1
                    #bottom left-right
                    for j in range(i,n-i):
                        l[n-i][j]=l[n-i][j-1]-1
                    # right top-bottom
                    for j in range(i,n-i+1):
                        l[j][n-i]=l[j-1][n-i]+1
            
                k-=2
        if n>1:
            if n%2:
                l[n//2][n//2]=l[n//2][n//2-1]+1
                l[n//2][n//2+1]=l[n//2-1][n//2+1]+1
                l[n//2+1][n//2-1]=l[n//2][n//2-1]-1
                l[n//2+1][n//2]=l[n//2+1][n//2-1]-1
                l[n//2+1][n//2+1]=l[n//2+1][n//2]-1
            else:
                l[n//2][n//2]=l[n//2][n//2-1]-1
        return l
