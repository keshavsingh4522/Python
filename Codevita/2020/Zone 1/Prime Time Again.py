def IsPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

d=dict()
D,P=map(int,input().split())
k=D
while k:
    d[k]=IsPrime(k)
    k-=1
H=D//P
N=H
res=0
while N>1:
    i=0
    count=0
    while True:
        k=H*i+N
        if d[k] and k<=D:
            count+=1
        else:
            break
        if i==(P-1):
            break
        i+=1
    if count==P:
        res+=1
    N-=1
print(res)