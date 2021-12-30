class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        visite = set()
        
        def helper(r,c,d):
            
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != 1:
                return 'O'
            
            grid[r][c] = 0 # mark as water
            
            path = ""
            path += d
            
            path += helper(r-1,c,"U")
            path += helper(r+1,c,"D")
            path += helper(r,c-1,"L")
            path += helper(r,c+1,"R")
            return path
        
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    visite.add(helper(i,j,'S'))
        
        return len(visite)
        