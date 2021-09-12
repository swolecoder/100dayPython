class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        l1 = len(nums)-1
        
        product = 1
        
        for num in nums:
            left.append(product)
            product = product * num
        
        print(left)
        
        ans = []
        
        product = 1
        for num in nums[::-1]:
            ans.append(product* left[l1])
            product = product * num
            l1 -=1
        
        print(ans)
        
        return ans[::-1]
        
        
        