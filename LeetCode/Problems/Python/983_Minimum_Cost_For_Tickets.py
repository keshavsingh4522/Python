class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        if(n == 1):
            return min(costs)

        dp = [0]*(n+1)

        for i in range(n):
    
            ans = dp[i] + costs[0]
            j = i
            for c, d in zip(costs[1:], [7, 30]):
                while j >= 0 and days[j] > days[i]-d:
                    j -= 1
                ans = min(ans, dp[j+1] + c)
            dp[i+1] = ans
        
        return dp[n]