'''
count number of pairs whose sum is divisible by 4
'''
# def default():
#     return 0
from collections import defaultdict
# a=list(map(lambda x: int(x)%4,input().split()))
a=list(map(int,input().split()))
n=len(a)
# d=defaultdict(default)
d=defaultdict(int)
i=0
while i<n:
    if d[a[i]%4]==[]:
        d[a[i]%4]=0
    else:
        d[a[i]%4]+=1
    i+=1
print(d[0]//2+d[1]*d[3]+d[2]//2)