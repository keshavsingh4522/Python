def binar(a,n):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(high+low)//2
        if a[mid]==n:
            return mid
        elif a[mid]<n:
            low=mid+1
        else:
            high=mid-1
    return low
a=[2, 3, 4, 10, 40,56,78,98]
n=int(input())
binar(a,n)