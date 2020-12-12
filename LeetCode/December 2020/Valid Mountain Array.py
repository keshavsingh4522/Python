#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/
class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        if len(a)<3:
            return False
        if a[0]>a[1]:
            return False
        
        d=0
        i=0
        k=0
        for j in range(len(a)-1):
            if a[j+1]>a[j]:
                if i==0:
                    i=1
                    k+=1
                    d=0
            elif a[j+1]<a[j]:
                if d==0:
                    k+=1
                    d=1
                    i=0
            else:
                return False
            if k>2:
                return False
        if k==2:
            return True
        return False
