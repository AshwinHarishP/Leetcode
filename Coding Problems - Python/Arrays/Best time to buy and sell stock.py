class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1 # i = buy and j = sell
        max_profit = 0

        while j < len(prices):

            if prices[i] < prices[j]:
                Profit = prices[j] - prices[i]
                max_profit = max(max_profit, Profit)
                
            else:
                i = j
            
            j += 1
        
        return max_profit
