class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        maxP = 0 
        

        for sell in prices:
            minBuy = min(sell, minBuy)
            maxP = max(maxP, sell - minBuy)
        
        return maxP