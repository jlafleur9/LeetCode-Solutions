class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        right = 1
        left = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                max_profit = max(max_profit, temp)
            else:
                left = right
            right += 1
        return max_profit