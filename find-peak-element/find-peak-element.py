class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        
        if not nums:
            return -1
        
        if len(nums) == 1:
            return 0
        
        while l <= r:
            
            mid = (l + r) // 2
            if mid + 1 < len(nums) and nums[mid]  < nums[mid +1]:
                l = mid +1
            else:
                r = mid -1
        
        
        print(l,r)
        
        return l
                
        