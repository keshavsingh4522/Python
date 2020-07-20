#https://www.hackerrank.com/challenges/mars-exploration/problem?h_r=next-challenge&h_v=zen
s=input()
s1='SOS'*(len(s)//3)
c=0
for i in range(len(s1)):
    if s[i]!=s1[i]:
        c+=1
print(c)