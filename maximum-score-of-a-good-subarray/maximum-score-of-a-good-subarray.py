class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        stack = []
        res = 0
        nums.append(0)
        for i in range(len(nums)):
            curr = nums[i]
            start = i
            
            while stack and stack[-1][1] >= curr:
                index, n = stack.pop()
                left = -1 if not stack else stack[-1][0]
                cal = k > left and k < i
                if cal:
                    total = start - left -1
                    res = max(res, total * n )
                # start = index
            
            stack.append((start, curr))

        print(stack)
        
        return res