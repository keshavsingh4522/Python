# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int, input().split()))
happy = 0
n = a[0]
m = a[1]
b = list(map(int, input().split()))
b = b[0:n]
c = list(map(int, input().split()))
c = c[0:m]
d = list(map(int, input().split()))
d = d[0:m]
for i in c:
    if b.count(i)!= 0:
        happy = happy + 1
for i in d:
    if b.count(i)!= 0:
        happy = happy - 1
print(happy)
