class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif max_profit <= prices[i] - min_price:
                max_profit = prices[i] - min_price
        return max_profit
