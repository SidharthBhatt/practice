class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max = 0 
        size = 0 
        l = 0
        for i,c in enumerate(s):
            while c in my_set:
                my_set.remove(str(s[l]))
                size-= 1
                l+= 1
            my_set.add(c)
            size += 1
            if (size > max):
                max = size
        return max
    
