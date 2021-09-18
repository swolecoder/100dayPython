from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(List)
        
        for i in range(len(nums)):
            if nums[i] not in self.map:
                self.map[nums[i]] = []
            self.map[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        
        val = self.map[target]
        
        i = random.randrange(len(val))
        
        return val[i]
        
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)