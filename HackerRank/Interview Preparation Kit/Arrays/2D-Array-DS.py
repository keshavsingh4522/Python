a=[]
for _ in range(6):
    a.append(list(map(int,input().split())))
sum_a=-9999999
for i in range(0,6-2):
    for j in range(0,6-2):
        temp=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        if temp>sum_a:
            sum_a=temp
print(sum_a)