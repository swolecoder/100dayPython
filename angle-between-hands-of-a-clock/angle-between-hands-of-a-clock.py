class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h =  (30 * hour) + 0.5 * minutes
        
        m = 6 * minutes
        
        print(h,m)
        
        ans = abs(h-m)
        
        if ans > 180:
            return 360 - ans
        
        return abs(h - m)