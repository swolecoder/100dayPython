class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0]* c for _ in range(r)]
        
        
        for row in range(r):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1
        
        for col in range(c):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1
        
        
        for i in range(1,r):
            for j in range(1,c):
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        
        return dp[-1][-1]
        
        
        