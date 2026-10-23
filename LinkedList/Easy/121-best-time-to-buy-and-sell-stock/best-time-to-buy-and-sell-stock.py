class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maximum_profit = 0 
        minimum = None
        maximum = None
        for price in prices:
            if minimum is None and maximum is None:
                minimum = price
                maximum = price
            elif price > maximum:
                maximum = price
            elif price < minimum:
                minimum = price
                maximum = price
            if maximum - minimum > maximum_profit:
                maximum_profit = maximum - minimum
        return maximum_profit


        