class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        left = 0
        for right in range(len(prices)):
            new_price = prices[right] - prices[left]
            max_profit = max(max_profit, new_price)
            if new_price < 0:
                left = right

        return max_profit
