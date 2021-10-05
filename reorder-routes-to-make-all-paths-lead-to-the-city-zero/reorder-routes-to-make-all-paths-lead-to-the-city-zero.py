class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        un_directed = {city:[] for city in range(n)}
        directed = {(a,b) for a,b in connections}
        
        print(directed)
        visited = set()
        ans = 0
        for a,b in connections:
            un_directed[a].append(b)
            un_directed[b].append(a)
            
        def dfs(city):
            nonlocal ans
            
            for nei in un_directed[city]:
                if nei in visited:
                    continue
                if nei not in visited:
                    
                    if (nei,city) not in directed:
                        ans +=1
                    
                    visited.add(nei)
                    dfs(nei)
        visited.add(0)
        dfs(0)
        return ans