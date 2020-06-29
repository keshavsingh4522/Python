n1,n2=map(int,input().split())
a=[]
for i in range(n2):
    a.append(list(map(float,input().split())))
for i in zip(*a):
    print(sum(i)/n2)