class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        if prices[0] > prices[1]:
            min = [prices[1]]
            max = [prices[1]]
        else:
            min = [prices[0]]
            max = [prices[1]]
        min_pos = 0
        max_pos = 0
        max_profit = 0
        for i in range(2,len(prices)):
            if prices[i] < min[min_pos]:
                min.append(prices[i])
                max.append(prices[i])
                min_pos += 1 
            else:
                max.append(prices[i]) 
                min.append(min[min_pos])
                max_pos += 1
                min_pos += 1
        
        if len(max) > len(min):
            length = len(min)
        else:
            length = len(max)
        print(min)
        print(max)
        for i in range(length):
            if max[i] - min[i] > max_profit:
                max_profit = max[i] - min[i]
        return max_profit


        