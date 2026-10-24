from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i_index, i in enumerate(nums):
            hash_map[target - i ] = i_index
        for v_index, v in enumerate(nums):
            try:
                 if v_index != hash_map[v]:
                    return [hash_map[v], v_index]
            except: 
                pass