class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        open, extra = 0, 0
        
        for i in range(len(s)):
            if s[i] == "(":
                open +=1
            else:
                
                if not open:
                    extra +=1
                else:
                    open -=1
        return open + extra 
        