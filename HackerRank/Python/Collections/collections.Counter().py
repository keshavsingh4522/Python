#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
input()
a=list(map(int,input().split()))
c=Counter(a)
count=0
for i in range(int(input())):
    n1,n2=input().split()
    if c[int(n1)]:
        count+=int(n2)
        c-=Counter([int(n1),])
print(count)