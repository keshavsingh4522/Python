#ef getMinDiff( arr):
    c = []
    length = len(arr)
    for i in range(0, length - 1):
        temp = arr[i + 1] - arr[i]
        c.append(temp)
    maximum = max(c)
    minimum=min(c)
    result=maximum-minimum

    print(c)
    print(result)

arr = [1, 5, 8, 10]
getMinDiff(arr)
