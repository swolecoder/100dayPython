class Solution:
    def maxDepth(self, s: str) -> int:
        
        
        open = 0
        maxopen = 0
        
        for i in range(len(s)):
            
            if s[i] == '(':
                open +=1
            elif s[i] == ")":
                maxopen = max(maxopen, open)
                open -=1
        
        return maxopen
                