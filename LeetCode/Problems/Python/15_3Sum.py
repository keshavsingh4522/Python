class Solution:
    def threeSum(self, nums):
        res = set()
        targets_dict = {}
        
        nums.sort()
        
        for i, num in enumerate(nums):
            targets_dict = {}
            target = -num
            if(i>0 and nums[i] == nums[i-1]):
                continue
            for num2 in nums[i+1:]:
                if(num2 in targets_dict):
                    res.add((num, num2, targets_dict[num2]))
                targets_dict[target-num2] = num2 

        return res