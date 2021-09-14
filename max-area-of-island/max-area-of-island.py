class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return 0
            
            count = 1
            
            seen = grid[r][c]
            
            grid[r][c] = 0
            
            count += dfs(r-1,c) + dfs(r+1,c)+dfs(r, c-1)+dfs(r, c+1)
            return count
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
                    
        return ans
                    
        