class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        map = {}
        def dfs(i):
            
            if i == len(days):
                return 0
            
            if i in map:
                return map[i]
            res = float('inf')
            for day, cost in zip([1,7,30], costs):
                print(day,cost)
                j = i
                
                while j < len(days) and days[j] < days[i]+day:
                    j +=1
                
                res = min(res,dfs(j)+cost)   
                
            map[i] = res    
            return res
         
        return dfs(0)
        