#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        c=1
        if k==1:
            return 1
        for i in range(2,n//2+1):
            if n%i==0:
                c+=1
            if c==k:
                return i
        if (c+1)==k:
            return n
        return -1
