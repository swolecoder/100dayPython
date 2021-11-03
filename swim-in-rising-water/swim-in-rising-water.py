from heapq import heappush,heapify,heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        target = (len(grid)-1, len(grid[0])-1)
        
        R = len(grid)
        C = len(grid[0])
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        seen = set()
        heap = [[grid[0][0], 0,0]]
        # heap = heapify(h)
        
        
        while heap:
            
            h,r,c = heapq.heappop(heap)
            print(h,r,c)
            if (r,c) == target:
                return h
            
            for dx,dy in dirs:
                
                newR = r + dx
                newC = c + dy
                
                
                if  0<=newR <R and 0 <= newC < C and (newR,newC) not in seen:
                    data = max(grid[newR][newC],h)
                    heapq.heappush(heap,[max(grid[newR][newC],h),newR, newC])
                    seen.add((newR,newC))
                
                
        