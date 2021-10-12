class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        count_zero = s.count("0")
        
        ones = 0
        
        ans = count_zero
        
        for i in s:
            
            if i == "0":
                count_zero -=1
            else:
                ones +=1
            ans = min(ans,count_zero + ones)
            
        return ans
                
        