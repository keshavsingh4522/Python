class Solution:
    def distributeCandies(self, c: int, n: int) -> List[int]:
        d=[0 for i in range(n)]
        i=0
        while c:
            if c>i+1:
                d[i%n]+=i+1
                c-=i+1
            else:
                d[i%n]+=c
                c=0
            i+=1
        return d
