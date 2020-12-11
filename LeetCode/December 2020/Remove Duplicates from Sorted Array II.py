#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/
class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        d=dict()
        c=0
        for i in range(len(a)):
            try:
                d[a[i-c]]+=1
                if d[a[i-c]]>2:
                    a.pop(i-c)
                    c+=1
            except:
                d[a[i-c]]=1
        return len(a)
