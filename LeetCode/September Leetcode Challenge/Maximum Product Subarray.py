# o(1) space complexity o(n) time complexity
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/
def result(a):
    n=len(a)
    if n==0:
        return -1
    if n==1:
        return a[0]

    ans=a[0]
    max_p=a[0]
    max_n=a[0]

    for i in range(1,n):
        choice1=max_n*a[i]
        choice2=max_p*a[i]
        max_n=min(a[i],choice1,choice2)
        max_p=max(a[i],choice1,choice2)
        ans=max(max_n,max_p,ans)
    return ans

a=list(map(int,input().split()))
ans=result(a)
print(ans)
