class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        res = dp[0]
        for i in range(1,len(dp)):
            dp[i] = max(dp[i], dp[i]+ dp[i-1])
            res = max(dp[i], res)
        return res