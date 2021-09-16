class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        open = 0
        extra = 0
        
        
        for i in range(len(s)):
            curr = s[i]
            
            if curr == "(":
                open +=1
            else:
                if open <=0:
                    extra +=1
                else:
                    open -=1
        
        return open + extra
        