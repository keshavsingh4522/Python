'''
find missing numbers in array
given: array having N-1 elements
range: 1-N
'''
from collections import defaultdict
N=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
i=0
while i<N-1:
    d[a[i]]=1
    i+=1
i=1
while i<=N:
    if d[i]==0:
        print(i)
        break
    i+=1