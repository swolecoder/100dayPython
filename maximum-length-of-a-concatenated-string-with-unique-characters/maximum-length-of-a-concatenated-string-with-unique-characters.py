from collections import Counter
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        visited = set()
        
        def unique(a,b):
            s = Counter(a) + Counter(b)
            
            return max(s.values()) > 1

        
        
        def dfs(i):
            
            if i == len(arr):
                #do stuff
                print(visited)  
                return len(visited)
             
            res = 0 
            if not unique(visited, arr[i]):
                for c in arr[i]:
                    visited.add(c)
            
                res = dfs(i+1)
            
                for c in arr[i]:
                    visited.remove(c)
                # notInclude = dfs(i+1)
            
                # res = max(include, notInclude)
            
            return max(res, dfs(i+1))
        
        return dfs(0)