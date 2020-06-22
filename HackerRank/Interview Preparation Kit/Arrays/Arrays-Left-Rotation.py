a1,a2=input().split()
a=list(map(int,input().split()))
for i in range(int(a2)):
    a.append(a.pop(0))
print(a)