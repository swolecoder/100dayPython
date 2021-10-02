class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        
        visited = { s for s in nums} 
        
      
        def dfs(i, curr):
            
            if i == len(nums):
                a = "".join(curr)
                print(a)
                return None if a in visited else a
        
            res = dfs(i +1, curr)
            if res:return res 
            
            curr[i] = "1"
            res = dfs(i+1, curr)
             
            if res:return res
        
        return dfs(0, [ "0" for s in  nums])