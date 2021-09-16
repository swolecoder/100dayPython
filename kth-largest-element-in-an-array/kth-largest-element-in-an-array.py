class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        print(nums)
        return nums[-k]
        