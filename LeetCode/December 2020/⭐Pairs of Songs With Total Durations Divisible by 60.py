class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c=0
        d=dict()
        for i in time:
            try:
                d[i%60]+=1
            except:
                d[i%60]=1
        for i in range(1,30):
            try:
                c+=d[i]*d[60-i]
            except:
                pass
        try:
            c+=d[30]*(d[30]-1)//2
        except:
            pass
        try:
            c+=d[0]*(d[0]-1)//2
        except:
            pass
        return c
