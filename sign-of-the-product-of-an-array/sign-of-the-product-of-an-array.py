class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        zero = 0
        neg = 0
        
        for n in nums:
            if n == 0 : zero +=1
                
            if n < 0:
                neg +=1
        
        
        if zero > 0 :
            return 0
        
        if neg % 2 == 0:
            return 1
        
        return -1
        