class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        ans = 1
        
        if n == 1:
            return True
        
        while ans  <= n:
            ans = ans * 3
            
            if ans == n:
                return True
        
        
        return False
        