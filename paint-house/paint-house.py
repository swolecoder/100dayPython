class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        map = {}
        def dfs(index,pre):
            
            # print("Ashishj")    
            if index == len(costs):
                # print(data)
                return 0
            
            if (index, pre) in map:
                return map[(index,pre)]
            
            ans = float('inf')
            for d in range(len(costs[index])):
                
                if d == pre:
                    continue
                
                ans = min(ans,costs[index][d] +dfs(index+1,d) )
                print(ans)
            map[(index,pre)] = ans
            return ans

            
            
            
        return dfs(0,-1)
        