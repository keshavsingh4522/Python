def Linearsearch(arr, x):

	for i,item in enumerate(arr):

		if arr[i] == x:
			return i

	return -1

arr = [4,0,9,5,1,3]
print(Linearsearch(arr, 5))