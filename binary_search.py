def binary_search():
    """
    Perform binary search on a sorted array to find the index of the target element.
    If the target element is not found, return -1.
    """
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = int(input("Enter the target element: "))
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search())
