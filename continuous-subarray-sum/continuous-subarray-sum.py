class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        map = {0:-1}
        
        sum = 0
        
        for i in range(0, len(nums)):
            sum +=nums[i]
            per = sum % k 
            
            if per in map:
                if i - map[per] >=2:
                    return True
            else:
                map[per] = i
        
        
        return False
        