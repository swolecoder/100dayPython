class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        alt = set()
        
        row = len(heights)
        col = len(heights[0])
        
        def dfs(r,c,visited,prev):
            
            if r < 0 or c < 0 or r >=row or c >= col or heights[r][c] < prev or (r,c) in visited:
                return 
            
            prev = heights[r][c]
            visited.add((r,c))
            
            dfs(r+1, c, visited, prev)
            dfs(r-1, c, visited, prev)
            dfs(r, c+1, visited, prev)
            dfs(r, c-1, visited, prev)
        
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,alt,heights[row-1][c])
            
        
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,alt,heights[r][col-1])
            
        
        ans = []
        
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in alt:
                    ans.append([r,c])
        return ans