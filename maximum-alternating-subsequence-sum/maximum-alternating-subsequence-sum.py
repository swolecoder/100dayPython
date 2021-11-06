class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        maxAns = float('-inf')
        map = {}
        def dfs(index, even):
            if index == len(nums):
                return 0
            
            if (index, even) in map:
                return map[(index, even)]
            total = nums[index] if even else -1 * nums[index]
            map[(index, even)] = max ( total + dfs(index+1, not even), dfs(index +1,even))
            
            return map[(index, even)]
        
        
        return dfs( 0,True)
            
            
            
#         def dfs(i,flag,total):
#             nonlocal maxAns
#             if i == len(nums):
#                 # print(total)
#                 maxAns = max(maxAns,total)
#                 return total
#             if (i,flag) in map:
#                 return map[(i,flag)]
            
            
#             # res = float('inf')
#             checker = total + nums[i] if flag else total + (-1 * nums[i])
#             map[(i,flag)] = max(dfs(i+1,not flag,  checker),  dfs(i+1,flag, total))
#             # dfs(i+1,not flag,  checker)
#             # dfs(i+1,flag, total) #skip
#             return  map[(i,flag)]

      
        
        
        
        
        
        
        
        
        
        # return dfs(0,True,0)
        # return maxAns
                