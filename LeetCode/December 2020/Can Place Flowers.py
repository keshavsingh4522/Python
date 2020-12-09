#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/
class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        i=0
        count=0
        while i<len(a):
            if i==0:
                try:
                    if a[i]==0 and a[i+1]==0:
                        count+=1
                        a[i]=1
                except:
                    if a[i]==0:
                        count+=1
            elif i==(len(a)-1):
                if a[i-1]==0 and a[i]==0:
                    count+=1
                    a[i]=1
            else:
                if a[i-1]==0 and a[i+1]==0 and a[i]==0:
                    count+=1
                    a[i]=1
            i+=1
        if count>=n:
            return True
        return False
