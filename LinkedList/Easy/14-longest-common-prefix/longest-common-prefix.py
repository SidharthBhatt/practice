class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        sol = ""
        
        for a in range(len(strs[0])):
            prev = strs[0][a]
            for b in range(1,len(strs)):
                if a >= len(strs[b]):
                    return sol
                if strs[b][a] != prev:
                    return sol
            sol += (prev)
        return sol
        