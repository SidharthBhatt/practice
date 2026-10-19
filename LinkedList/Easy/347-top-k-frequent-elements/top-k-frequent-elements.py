from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else: 
                dictionary[i] = 1 
        flipped_dictionary = defaultdict(list)
    
        for number, frequency in dictionary.items():
            flipped_dictionary[frequency].append(number)

        count = k
        ans = []
        for frequency in range(len(nums), 0, -1):
            if frequency in flipped_dictionary:
                for number in flipped_dictionary[frequency]:
                    if count > 0:
                        ans.append(number)
                        count -= 1
                        if count == 0: 
                            return ans
                    else:
                        return ans
        

                
        return ans




        