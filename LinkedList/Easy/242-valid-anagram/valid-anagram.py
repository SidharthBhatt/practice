
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        logic = True 
        length = len(s)
        if len(t) != length:
            return False
        dictS = {}
        dictT = {}
        for i in range(length):
            try:
                dictS[s[i]]
                dictS[s[i]] += 1
            except: 
                 dictS[s[i]] = 1
            try:
                dictT[t[i]]
                dictT[t[i]] += 1
            except: 
                 dictT[t[i]] = 1
        
        return dictS == dictT
            
        