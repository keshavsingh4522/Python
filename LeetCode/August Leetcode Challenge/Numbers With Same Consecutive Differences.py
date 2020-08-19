# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/
class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        res=[]
        if n==1:
            res.append(0)
        def dfs(num,n):
            if n==0:
                res.append(num)
                return
            lsd=num%10
            if lsd>=k:dfs(num*10+lsd-k,n-1)
            if k>0 and lsd+k<10:dfs(num*10+lsd+k,n-1)
        for d in range(1,10):
            dfs(d,n-1)
        return res
