class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        prev = -20000
        for index_i, i in enumerate(numbers): 
            complement =  target - i
            if numbers[index_i] == prev:
                pass
            else:      
                for index_j in range(index_i+1,len(numbers)):
                    try:
                        if numbers[index_j] == complement: 
                            return [index_i+1, index_j+1]
                        # elif abs(numbers[index_j]) > abs(target): 
                        #     break; 
                    except: 
                        break
                prev = numbers[index_i]
        

        