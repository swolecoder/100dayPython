class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        N = len(prices)
        def dfs(index,buy):
            if index >= N:
                return 0
            
            if (index,buy) in dp:
                return dp[(index, buy)]
            
            res = float("-inf")
            # for i in range(index, N):
                
            if buy:
                    
                    buying = dfs(index+1,not buy) - prices[index]
                    cooldown = dfs(index+1, buy)
                    # res = max(res,max(buying,cooldown) )
                    dp[(index,buy)] = max(buying,cooldown)
                    # return max(buying,cooldown)
            else:
                    
                    sell = dfs(index+2,not buy) + prices[index]
                    cooldown = dfs(index+1, buy)
                    # res = max(res,max(sell,cooldown))
                    dp[(index,buy)] = max(sell,cooldown)
                    # print(res)
            
            # return res
            return dp[(index,buy)]
        
                
            
            
        return dfs(0,True)
        