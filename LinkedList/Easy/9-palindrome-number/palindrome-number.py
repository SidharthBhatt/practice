import math 
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # string method
        # temp = str(x)
        # reverse = temp[::-1]
        # return bool(temp == reverse)
        
        # pure math method 
        if x < 0:
            return False
        if x < 10:
            return True; 
        temp = x
        reverse = 0
        length = math.floor(math.log10(x))+1
        for i in range(math.floor(length/2)):
            reverse = reverse*10 + temp%10 
            temp = math.floor(temp/10)
        if (length % 2 == 0): 
            return bool(reverse -  temp == 0)
        temp = math.floor(temp/10) # remove middle digit if the # of digits is odd
        return bool(reverse -  temp == 0)
    
        