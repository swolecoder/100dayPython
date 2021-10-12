class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] *(len(nums)) 
        
        ans = float('-inf')
        
        for i in range(len(dp)):
            val = 0 if i-1 < 0 else dp[i-1]
            val2 = nums[i] if i-2 < 0 else nums[i]+dp[i-2]
            dp[i] = max(val, val2 )
            ans = max(ans, dp[i])
            
        print(dp)
        return ans
        