class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        N = len(grid[0])

        prefix1, prefix2 = grid[0].copy(), grid[1].copy()
        
        for i in range(1, N):
            prefix1[i] += prefix1[i-1]
            prefix2[i] += prefix2[i-1]
        
        first = float('inf')
        for i in range(N):
            top =  prefix1[-1] - prefix1[i]
            bottom = prefix2[i-1] if i > 0 else 0
            print(top,bottom)
            second = max(top,bottom)
            
            first = min(first,second)
            
        return first
            
        