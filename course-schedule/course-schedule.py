class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        map = { i: [] for i in range(numCourses)}
        
        print(map)
        
        
        for cource,pre in prerequisites:
            map[pre].append(cource)
            
        
        print(map)
        
        
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            if map[node] == []:
                return True
            
            visited.add(node)
            
            for pre in map[node]:
                
                if not dfs(pre):
                    return False
            
            visited.remove(node)
            map[node] = []
            return True
            
            
        for i in range(numCourses):
            if not dfs(i):return False
            
        return True
            
            