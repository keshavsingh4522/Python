from collections import Counter
c=Counter()
for _ in range(int(input())):
    n1,n2=map(int,input().split())
    if n1==1:
        c+=Counter([n2])
    if n1==2:
        c-=Counter([n2])
    if n1==3:
        if n2 in c.values():
            print(1)
        else:
            print(0)