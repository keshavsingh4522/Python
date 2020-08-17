''' find pair whose sum is equal to target sum '''

from collections import defaultdict
n=int(input())
a=defaultdict(list)

a1=list(map(int,input().split()))
le=len(a1)

i=0
while i<le:
    a[a1[i]]=i
    i+=1

i=0
while i<le:
    if a[n-a1[i]]!=[]:
        print(i,a1[i],n-a1[i])
        break
    i+=1