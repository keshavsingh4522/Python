'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while(l<r):
                sum = nums[i] + nums[l] + nums[r]
                if sum<0:
                    l+=1
                elif sum >0:
                    r-=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
                    while r>0 and nums[r] == nums[r - 1]: r -= 1
                    l+=1
                    r-=1
        return result
ob1 = Solution()
print(ob1.threeSum([1,-1,-1,0]))