class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        d = deque([])#decreasing order
        ans =[]
        
        l,r =0,0
        
        #monotnic decreaidsn 
        while r < len(nums):
            
            curr = nums[r]
            
            
            while d and nums[d[-1]] < curr:
                d.pop()
            
            d.append(r)
            if l > d[0]:
                d.popleft()
            
            
            if r +1 >=k:
                ans.append(nums[d[0]])
                l +=1
            
            r +=1
        print(ans)
        
        return ans