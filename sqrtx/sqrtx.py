import math
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        l , r = 2, x//2
        
        while l <=r:
            
            middle = (l +r) //2
            
            num = pow(middle,2)
            
            if num < x:
                l = middle + 1
            elif num > x:
                r = middle -1
            else:
                return middle
            
        return r
        