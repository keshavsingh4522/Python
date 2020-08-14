# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423/
from collections import defaultdict
d=defaultdict(list)
s=input()
n=len(s)
i=0
while i<n:
    d[s[i]]=d.get(s[i],0)+1
    i+=1
count=0
i=0
for j in set(s):
    if d[j]>1:
        if d[j]%2==0:
            count+=d[j]
        else:
            count+=d[j]-1
            i=1
    else:
        i=1
print(count+i)