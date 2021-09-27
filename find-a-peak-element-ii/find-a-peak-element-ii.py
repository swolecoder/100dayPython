class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        r = len(mat)
        c = len(mat[0])
        
        def valid(i,j):
            if i < 0 or j < 0 or i >= r or j >= c:
                return -1
            else:
                return mat[i][j]
    
        for i in range(r):
            for j in range(c):
                top = valid(i-1,j)
                bottom = valid(i+1,j)
                left = valid(i,j-1)
                right = valid(i,j+1)
                currentNum = mat[i][j]
                if currentNum > top and currentNum > bottom and currentNum > left and currentNum> right:
                    return [i,j]
        
        
        
        return [-1,-1]