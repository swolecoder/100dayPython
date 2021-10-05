from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        row, col = len(grid), len(grid[0])
        ans = 0
        visited = set()
        
        
        def bfs(r, c):
            visited.add((r,c))
            q = deque()
            q.append((r,c))
            while q:
                r1,c1 = q.popleft()
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
                
                for dr, dc in directions:
                    new_r = r1 + dr
                    new_c = c1 + dc
                    
                    
                    if (new_r  in range(row)) and (new_c  in range(col)) and grid[new_r][new_c]=="1" and ((new_r, new_c) not in visited):
                        q.append((new_r, new_c))
                        print((new_r,new_c))
                        grid[new_r][new_c]=="0"
                        visited.add((new_r,new_c))
                
        
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i,j)
                    ans +=1
                    
                    
        print(visited)
        return ans