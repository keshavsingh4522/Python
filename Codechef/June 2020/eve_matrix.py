# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=1
    for i in range(n):
        for j in range(n):
            if i%2==0:
                print(c,end=' ')
                c+=1
            else:
                print(c+n-j-1,end=' ')
        else:
            if i%2!=0:
                c+=n
        print()