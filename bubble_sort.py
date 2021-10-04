arr=[5,8,9,6,4,8,9,1]
n=len(arr)
for i in range(0,n-1):
    for j in range(0,n-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
