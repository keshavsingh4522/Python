for _ in range(int(input())):
    n1,k=input().split()
    k=int(k)
    a=map(int,input().split())
    l=[]
    for i in a:
        if k%i==0:
            l.append(i)
    l.sort(reverse=True)
    if len(l)==0:
        print(-1)
    else:
        print(l[0])
