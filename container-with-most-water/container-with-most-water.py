class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        
        i =0
        j = len(height)-1
        
        while i <j :
            
            minH = min(height[i], height[j])
            maxarea = max(minH * (j-i), maxarea)
            
            if height[i] < height[j]:
                i +=1
            else:
                j -=1
            
         
        return maxarea
        