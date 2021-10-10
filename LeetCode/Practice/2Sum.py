class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        d={}
        for i in range(0,len(nums)):
            if nums[i] in d:
                ans.append(d[nums[i]])
                ans.append(i)
            else:
                d[target-nums[i]]=i
        return ans