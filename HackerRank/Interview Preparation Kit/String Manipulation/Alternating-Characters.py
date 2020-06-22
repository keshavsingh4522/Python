for _ in range(int(input())):
    s=input()
    if len(s)==1:
        print(0)
    else:
        c=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
    print(c)