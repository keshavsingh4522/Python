class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        peak=prices[0]
        valley=prices[0]
        profit=0
        for i in range(0,len(prices)-1):
            if prices[i+1]<prices[i]:
                valley=prices[i+1]
            elif prices[i+1]>prices[i]:
                peak=prices[i+1]
                profit+= peak-valley
                valley=peak
               # print(peak,valley)
        return profit