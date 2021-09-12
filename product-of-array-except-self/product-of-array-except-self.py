class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        left = []
        product = 1
        for num in nums:
            left.append(product)
            product = product * num
        
        
        product = 1
        
        length = len(nums)-1
        
        ans = []
        for num in nums[::-1]:
            ans.append(product * left[length])
            length -=1
            product = product * num
        
        return ans[::-1]
            
            
        