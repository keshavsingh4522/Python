class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                temp=prices[i]-buy
                if temp>profit:
                    profit=temp
        return profit