class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        
        def dfs(index, data, currentsum):
            if index > len(candidates)-1 or currentsum > target:
                return
            
            if currentsum == target:
                res.append(data.copy())
                return
            
            
            
                #we include the number
            data.append(candidates[index])
            dfs(index, data, currentsum + candidates[index])
                
                #not include
            data.pop()
            dfs(index+1, data, currentsum)
                
                
        dfs(0,[], 0)   
        
        print(res)
        
        return res
        