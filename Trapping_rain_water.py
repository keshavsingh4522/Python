'''
A program to find the maximum amount of water that can be trapped within given set of bars.
Time Complexity: O(n)
Space Complexity : O(1)
'''
def findWater(arr, n):
    result = 0
    left_max = 0
    right_max = 0
    low = 0
    high = n-1
      
    while(low <= high):
        if(arr[low] < arr[high]):
            if(arr[low] > left_max):
                left_max = arr[low]
            else:
                result += left_max - arr[low]
            low+= 1
         
        else:
            if(arr[high] > right_max):
                right_max = arr[high]
            else:
                result += right_max - arr[high]
            high-= 1
         
    return result
 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
 
print("Maximum water that can be trapped is ", findWater(arr, n))