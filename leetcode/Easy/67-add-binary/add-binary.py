import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        c = ""
        carry = 0 
        for i in range(max(len_a,len_b)):
            a_pos = len_a-i-1
            b_pos = len_b-i-1
            a_val = 0 
            b_val = 0
            if a_pos >= 0:
                a_val = int(a[a_pos])
            if b_pos >= 0:
                b_val = int(b[b_pos])
            digit = math.floor(a_val + b_val + carry)
            c += str(digit%2)
            carry = math.floor(digit/2)

        if carry > 0:
            c += str(carry)
        return c[::-1]



