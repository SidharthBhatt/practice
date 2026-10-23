class Solution:
    def isValid(self, s: str) -> bool:
        que = ""
        converter = {')' : '(', '}': '{', ']' : '['}
        startings = {'(', '{', '['}
        for c in s:
            if c in startings:
                que+=c
            elif len(que) == 0:
                return False
            elif converter[c] in que[len(que)-1:]:
                que = que[:len(que)-1]
            else:
                return False
        if len(que) == 0:
            return True
        else:
            return False




        