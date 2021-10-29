class Solution:
    def twoSum(self, nums, target):
        targets_dict = {}
        
        for i, num in enumerate(nums):
            if(num in targets_dict):
                return [targets_dict[num], i]
            targets_dict[target-num] = i
        
        # we do not need to return because we assume that
        # we have exactly one solution
        # return -1
