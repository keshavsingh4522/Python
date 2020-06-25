for _ in range(int(input())):
    n=int(input())
    x=bin(n)[2:]
    s=''
    for i in x:
        if i=='0':
            s+='1'
        else:
            s+='0'
    print(int('1'*(32-len(x))+s,2))