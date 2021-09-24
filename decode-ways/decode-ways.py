class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
      
        dp[1] = (0 if int(s[0]) == 0 else 1)
        if len(s) == 1:
            return dp[-1]
        
        for i in range(2, len(dp)):
            oneway = s[i-1]
            twoway = s[i-2:i]
            print(oneway,twoway)
            if int(oneway) > 0 and int(oneway)  <= 9:
                dp[i] += dp[i-1]
            
            if int(twoway) >= 10 and int(twoway)  <=26:
                dp[i] += dp[i-2]
                
        
        
        print(dp)
        
        return dp[-1]