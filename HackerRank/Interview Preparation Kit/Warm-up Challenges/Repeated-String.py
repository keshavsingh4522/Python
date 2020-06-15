s=input()
n=int(input())
print(s.count('a')*(n//len(s))+s[:n%len(s)].count('a'))