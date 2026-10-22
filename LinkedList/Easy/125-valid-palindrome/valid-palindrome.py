import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = []
        for c in s:
            if c.isalnum():
                cleaned.append(c)
        length = len(cleaned)
        half = length//2 
        for i in range(0,half):
            if cleaned[i] != cleaned[length-1-i]:
                return False
        return True