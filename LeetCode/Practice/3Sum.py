class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums)):
            left=i+1
            right=len(nums)-1
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            while(left<right):
                    if(nums[left]+nums[right]+nums[i]==0):
                            temp=[nums[left],nums[right],nums[i]]
                            ans.append(temp)
                            while(left<len(nums)-1 and nums[left] == nums[left+1]):                                         
                                left=left+1
                            while(right > 0 and nums[right] == nums[right-1]):
                                right=right-1
                            left=left+1
                            right=right-1
                    elif((nums[left]+nums[right]+nums[i])>0):
                            right=right-1
                    else:   left=left+1       
        return ans
    