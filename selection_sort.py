arr=[5,8,9,6,4,8,9,1]
n=len(arr)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if(arr[min]>arr[j]):
            min=j
            arr[min],arr[i]=arr[i],arr[min]
print(arr)
