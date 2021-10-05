class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        row = len(grid)
        col = len(grid[0])
        
        def dfs(r,c):
            
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return 1
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            
            
            res = dfs(r+1,c)
            
            res += dfs(r-1,c)
            res += dfs(r,c+1)
            res += dfs(r,c-1)
            
            return res
        
            
            
        for r in range(row):
            for c in range(col):
                print("hellop")
                if grid[r][c]:

                    return dfs(r,c)
            
            
            
        return 0
        