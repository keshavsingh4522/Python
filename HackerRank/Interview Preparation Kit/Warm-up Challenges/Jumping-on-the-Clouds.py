n=int(input())
a=list(map(int,input().split()))
jump=0
i=0
while i<=n:
    if i+2<n and a[i+2]==0:
        jump+=1
        i+=2
    elif i+1<n and a[i+1]==0:
        jump+=1
        i+=1
    else:
        i+=1
print(jump)