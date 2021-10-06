class Solution:
    def integerReplacement(self, n: int) -> int:
        
        
        def dfs(n, count):
            
            if n <=1:
                return count
            
            if n % 2 == 0:
                return dfs(n//2,count+1)
            else:
                return min(dfs(n+1,count+1),dfs(n-1,count+1))
        
        return dfs(n,0)
        