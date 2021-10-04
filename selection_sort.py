arr=[5,8,9,6,4,8,9,1]
n=len(arr)
for i in range(n-1):
    minx=i
    for j in range(i+1,n):
        if(arr[minx]>arr[j]):
            minx=j
            arr[minx],arr[i]=arr[i],arr[minx]
print(arr)
