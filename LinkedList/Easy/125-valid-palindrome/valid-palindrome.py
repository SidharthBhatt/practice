class Solution:
    def isPalindrome(self, s: str) -> bool:
        posA = 0
        posB = len(s)-1
        while posA < posB:
            if s[posA].isalnum() and s[posB].isalnum():
                if s[posA].lower() != s[posB].lower():
                    return False
                else:
                    posA+= 1
                    posB-= 1 
            elif not s[posA].isalnum() and not s[posB].isalnum():
                posA+= 1
                posB-= 1
            elif s[posB].isalnum():
                posA+= 1
            else:
                posB-= 1
        return True