class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])
        seen = set()
        
        
        def dfs(r,c):
            
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in seen or grid2[r][c] == 0:
                return True
            
            seen.add((r,c))
            
            res = True
            if grid1[r][c] == 0:
                res = False
                
            res = dfs(r+1,c) and res
            res =  dfs(r-1,c) and res
            res = dfs(r,c+1) and res
            res =  dfs(r,c-1) and res
            
            
            
            return res
        
        
        count = 0
        
        for r in range(row):
            for c in range(col):
                
                if grid2[r][c] == 1 and (r,c) not in seen and dfs(r,c)  :
                    count +=1
        return count
            
            
                  
        