# https://www.codechef.com/AUG20B/problems/CHEFWARS
for _ in range(int(input())):
    a1,a2=map(int,input().split())
    k=0
    while a2:
       k+=a2
       a2//=2
    if a1>k:
        print('0')
    else:
        print('1')
