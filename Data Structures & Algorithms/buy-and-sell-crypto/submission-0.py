class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        max_num = prices[0]
        max_profit = 0
        for price in prices: 
            if price < min_num:
                min_num = price
                max_num = price
            else:
                max_num = price
                max_profit = max(max_profit, max_num - min_num)
        return max_profit