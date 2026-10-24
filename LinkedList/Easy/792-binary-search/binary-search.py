class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1 
        while start <= end: 
            mean = (end + start)//2 
            if nums[mean] == target:
                return mean 
            elif target > nums[mean]:
                start = mean + 1
            else:
                end = mean - 1
        return -1
        
        