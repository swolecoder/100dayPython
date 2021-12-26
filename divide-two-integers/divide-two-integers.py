class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        q,r = divmod(abs(dividend),abs(divisor))
        sign = 1
        
        if dividend * divisor < 0:
            sign = -1
        
        if sign * q >= 2147483648 :
            return sign * 2147483647
        
        if sign * q <= -2147483648:
            return -2147483648
        return sign * q
            
        