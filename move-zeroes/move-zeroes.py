class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left ,right =0,0
        n = len(nums)
        
        if n == 0 or n == 1:
            return 
        
        
        while right < n:
            
            if nums[right] == 0:
                right +=1
            else:
                
                nums[left],nums[right]=nums[right],nums[left]
                left +=1
                right +=1
        
        return 
                
                