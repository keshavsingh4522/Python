#https://www.hackerrank.com/challenges/caesar-cipher-1/problem
n_s=input()
s=input()
n=int(input())
s1=''
for i in s:
    if 65<=ord(i)<=90:
        s1+=chr((ord(i)-65)+n%26+65)
    elif 97<=ord(i)<=122:
        s1+=chr((ord(i)-97+n)%26+97)
    else:
        s1+=i
print(s1)