class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, total, data):
            if total > target or i > len(candidates)-1:
                return 
            if total == target:
                
                res.append(data.copy())
                print(data)
                return 
            
            
            data.append(candidates[i])
            dfs(i, total + candidates[i], data)
            data.pop()
            dfs(i+1, total,data)
                
                
        dfs(0,0,[])
        
        return res