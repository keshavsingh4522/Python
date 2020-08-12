# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/
k=int(input())
a=[]
for i in range(k+1):
    a.append(1)
    c=a.copy()
    for j in range(1,i):
        a[j]=c[j]+c[j-1]
#     print(a)
print(a)