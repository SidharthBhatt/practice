class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        half = length//2 
        posA = 0
        posB = length-1
        while posA < posB:
            if s[posA].isalnum() and s[posB].isalnum():
                if s[posA].lower() != s[posB].lower():
                    return False
                else:
                    posA+= 1
                    posB-= 1 
            elif s[posB].isalnum():
                posA+= 1
            else:
                posB-= 1
        return True