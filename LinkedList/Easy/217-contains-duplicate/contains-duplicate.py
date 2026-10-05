class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        logic = False
        dictionary = {}
        for num in nums:
            if num in dictionary:
                return True
            else:
                dictionary[num] = 1
        return False



        