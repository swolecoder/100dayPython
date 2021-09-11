# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        row, col = binaryMatrix.dimensions()
        print(row,col)
        
        ans = -1
        r = 0
        c = col-1
        
        while r < row and c >= 0:
            
            if binaryMatrix.get(r,c) == 0:
                r +=1
            else:
                ans = c
                c -=1
        
        print( c)
        return ans
        
        