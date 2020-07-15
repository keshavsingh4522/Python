#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
s=input()
p=0
for i in 'hackerrank':
    if i in s[p:]:
        p=s.index(i,p)+1
    else:
        print('NO')
        break
else:
    print('YES')