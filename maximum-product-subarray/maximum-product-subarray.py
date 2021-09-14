class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        minN , maxN = nums[0], nums[0]
        
        for i in range( 1, len(nums)):
            curr = nums[i]
            n1 = curr * minN
            n2 = curr * maxN
            minN = min(curr, n1 , n2)
            maxN = max(curr, n1 , n2)
            res = max(res, maxN)
        
        
        return res
        