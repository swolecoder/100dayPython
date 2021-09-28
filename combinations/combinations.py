class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        
        def dfs(index, total):
            # print(total)
            if len(total) > k  or index > n+1 :
                return 
            
            if len(total) == k:
                res.append(total.copy())
                return 
            
            for i in range(index,n+1):
                curr = i
                dfs(i +1 , total + [curr])
                
        dfs(1,[])  
        print(res)
        return res