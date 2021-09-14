class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        map = {}
        visited = set()
        
        islandId = 2
        
        def dfs(r, c):
        
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != 1:
                return 0
            
            count  = 0
            
            if (r,c) not in visited:
                visited.add((r,c)) # mark it as visited
                grid[r][c] = islandId
                count = 1 +  dfs(r-1,c) + dfs(r+1,c)+dfs(r, c-1)+dfs(r, c+1)

            return count
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    map[islandId] = dfs(i,j)
                    visited.clear() # clear set 
                    islandId +=1
                    
        print(map)
        
        ans = float("-inf")
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        ans = float('-inf')
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if not grid[i][j]:
                    cur = 0
                    cur_seen = set()
                    for move in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        next_i, next_j = i + move[0], j + move[1]
                        
                        if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] not in cur_seen and grid[next_i][next_j] > 0:
                            cur_seen.add(grid[next_i][next_j])
                            cur += map[grid[next_i][next_j]]
                            
                    ans = max(ans, cur + 1)

                            
                            
        return  ans if ans >0 else R * C          
        
        
        
        
        