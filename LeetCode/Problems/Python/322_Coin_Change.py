class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            ans = float('inf')
            for c in coins:
                if(i-c >= 0):
                    ans = min(ans, dp[i-c] + 1)
            dp[i] = ans



        return dp[-1] if dp[-1] != float('inf') else -1 # dp[amount+1]