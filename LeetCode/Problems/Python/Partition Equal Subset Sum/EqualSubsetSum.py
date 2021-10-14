class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # when sum is odd, then we can't divide in equal sum partition
        if sum(nums)%2 != 0:
            return False
        target_sum = int(sum(nums)/2)
        
        dp=[[False for j in range(target_sum+1)] for i in range(len(nums)+1)]
        dp[0][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, target_sum+1):
                if nums[i-1] > target_sum:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j-nums[i-1]] or dp[i-1][j])
        return dp[len(nums)][target_sum]
