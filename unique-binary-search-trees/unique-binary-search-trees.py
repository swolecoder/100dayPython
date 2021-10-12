class Solution:
    def __init__(self):
            self.map = {}
        

    def numTrees(self, n: int) -> int:

        if n <= 1:
            return 1
        
        if n in self.map:
            return self.map[n]
        count = 0
        for i in range(1, n+1):
            left = i-1
            right = n -i
            
            count += self.numTrees(left) * self.numTrees(right)
        
        self.map[n] = count
        return count
        