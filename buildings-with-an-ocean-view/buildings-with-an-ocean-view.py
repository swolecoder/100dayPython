class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        result = []
        maxH = float("-inf")
        
        for i in  range(len(heights)-1,-1,-1):
            if heights[i] > maxH:
                result.append(i)
            maxH = max(maxH, heights[i])
        
        return result[::-1]
        