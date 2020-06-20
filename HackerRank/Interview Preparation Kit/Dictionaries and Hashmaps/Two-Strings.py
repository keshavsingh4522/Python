for _ in range(int(input())):
    s1=input()
    s2=input()
    for i in s1:
        if i in s2:
            print('YES')
            break
    else:
        print('NO')
    print()