class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        map = {}
        
        def dfs(index, total):
            
            if (index, total) in map:
                return map[(index, total)]
            
            if index >= len(coins) or total >= amount:
                # print("Asjosh")
                return 0
            
            
            res = float('inf')
            for i in range(index,len(coins)):
                if (total + coins[i]) <= amount:
                    res = min(1 + dfs(i,total+coins[i]),res)
            
            map[(index, total)] = res
            return res
                
        
        a = dfs(0,0)
        return -1 if a == float('inf') else a
                
            
            
            
                
        