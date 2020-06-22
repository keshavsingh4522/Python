s=input()
l=list(set(s))
c=s.count(l[1])
i=1
k=0
for i in range(1,len(l)): 
    if s.count(l[i])==c or s.count(l[i])==(c+1) and k!=1:
        if  s.count(l[i])==(c+1)and k!=1:
            k+=1
    else:
        print('NO')
        break
else:
    print('YES')