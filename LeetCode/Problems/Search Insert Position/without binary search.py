a=[2, 3, 4, 10, 40,56,78,98]
n=int(input())
for i in range(len(a)):
    if a[i]>=n:
        print(i)
        break
else:
    print(i+1)