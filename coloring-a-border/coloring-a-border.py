class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        originalColor = grid[row][col]
        R = len(grid)
        C = len(grid[0])
        visited , ans = set(),set()
        def dfs(r,c):
            
            if r < 0 or c < 0 or r >= R or c >= C or (r,c) in visited:
                return 
            
            if grid[r][c] != originalColor:
                return 
            # is on the edge or node we poll has one differetn colot
            if r == 0 or c == 0 or r == R-1 or c == C-1 or grid[r-1][c] != originalColor or grid[r+1][c] != originalColor or grid[r][c-1] != originalColor or grid[r][c+1] != originalColor :
                ans.add((r,c))
            
            visited.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r, c-1)
            
            
        dfs(row,col)    
        print(ans)
        
        for r in range(R):
            for c in range(C):
                if (r,c) in ans:
                    grid[r][c] = color
        return grid
            
        