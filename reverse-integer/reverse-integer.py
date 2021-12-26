class Solution:
    def reverse(self, x: int) -> int:
        
        sum = 0
        
        sign  = 1
        
        if x < 0:
            sign = -1
            
            x = x * -1
            
        
        while x > 0:
            
            rem = x % 10
            
            sum = sum * 10 + rem 
            
            x = x//10
            
        if sum * sign  > (2 ** 31 - 1) or sum * sign < (- 2 ** 31):
            return 0
        return sum * sign 
        