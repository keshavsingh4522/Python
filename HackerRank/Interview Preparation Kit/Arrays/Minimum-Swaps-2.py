def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[i];
            arr[i] = arr[temp-1];
            arr[temp-1] = temp;  
            count +=1;
    return count;
n=int(input())
a=list(map(int,input().split()))
print(minimumSwaps(a))