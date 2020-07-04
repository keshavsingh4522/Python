def digit_sum(n):
    sum_n=0
    while n>0:
        r=n%10
        sum_n+=r
        n//=10
    return sum_n
for _ in range(int(input())):
    c1=0
    c2=0
    for i in range(int(input())):
        n1,n2=input().split()
        if digit_sum(int(n1))>digit_sum(int(n2)):
            c1+=1
        elif digit_sum(int(n1))<digit_sum(int(n2)):
            c2+=1
        else:
            c1+=1
            c2+=1
    if c1>c2:
        print('0',c1)
    elif c1<c2:
        print('1',c2)
    else:
        print('2',c1)