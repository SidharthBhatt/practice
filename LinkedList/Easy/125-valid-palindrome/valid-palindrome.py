import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        b = ""
        for i, c in enumerate(s):
            if c.isalnum():
                b += c
        s = b
        length = len(s)
        half = math.floor(length/2)
        for i in range(0,half):
            if s[i] != s[length-1-i]:
                return False
        return True