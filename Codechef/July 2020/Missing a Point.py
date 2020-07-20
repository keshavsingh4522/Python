from functools import reduce
for _ in range(int(input())):
    n=int(input())
    l1=[]
    l2=[]
    for i in range(4*n-1):
        m,n=map(int,input().split())
        l1.append(m) 
        l2.append(n)
    print(reduce(lambda x, y: x ^ y,l1),reduce(lambda x, y: x ^ y,l2))