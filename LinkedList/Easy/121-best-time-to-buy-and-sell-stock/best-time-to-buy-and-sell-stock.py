class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        if prices[0] > prices[1]:
            minimum = [prices[1]]
            maximum = [prices[1]]
        else:
            minimum = [prices[0]]
            maximum = [prices[1]]
        minimum_pos = 0
        maximum_pos = 0
        maximum_profit = 0
        for i in range(2,len(prices)):
            if prices[i] < minimum[minimum_pos]:
                minimum.append(prices[i])
                maximum.append(prices[i])
                minimum_pos += 1 
            else:
                maximum.append(prices[i]) 
                minimum.append(minimum[minimum_pos])
                maximum_pos += 1
                minimum_pos += 1
        
        for i in range(len(maximum)):
            if maximum[i] - minimum[i] > maximum_profit:
                maximum_profit = maximum[i] - minimum[i]
        return maximum_profit


        