from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        lookup = Counter(nums)
        
        sum = 0
        
        for k in lookup:
            if lookup[k] == 1:
                sum += k
        
        return sum
        
        
        