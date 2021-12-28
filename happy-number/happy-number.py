class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(d):
            totalSum = 0
            
            while d:
                tensP = d % 10
                totalSum += (tensP ** 2)       
                d = d //10
            return totalSum 
            

        visit = set()
        
        while n not in visit:
            
            visit.add(n)
            digit = helper(n)
            
            if digit == 1:
                return True
            
            
            n = digit
        
        
        return False
            
            
        
        
        
        
        