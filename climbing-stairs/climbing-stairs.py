class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        dp =  dp = [0 for i in range(n+1)]
        
        dp[0] =1
        dp[1] =1
        dp[2] =2
        
        for i in range(2,len(dp)):
            dp[i] = dp[i-1]+dp[i-2]
            
        print(dp)
        return dp[n]
        