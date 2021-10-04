def Linearsearch(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1