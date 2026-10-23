class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maximum_profit = 0 
        minimum = prices[0]
        for price in prices:
            if price < minimum:
                minimum = price
            if price - minimum > maximum_profit:
                maximum_profit = price - minimum
        return maximum_profit


        