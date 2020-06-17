n,m=map(int,input().split())
a=[]
a1=[[0]*n for _ in range(m)]
max_n=0
for i in range(m):
    a.append(list(map(int,input().split())))
for i in range(m):
    for j in range(n):
        if j>=a[i][0]-1 and j<a[i][1]:
            a1[i][j]=a[i][2]
        if i!=0:
            a1[i][j]+=a1[i-1][j]
        if a1[i][j]>max_n:
            max_n=a1[i][j]
print(a1,max_n,sep='\n')