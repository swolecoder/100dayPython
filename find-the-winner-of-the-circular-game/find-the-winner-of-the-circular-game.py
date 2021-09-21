from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        pq = deque([])
        
        for i in range(n, 0,-1):
            pq.append(i)
        
        print(pq)
        
        
        while len(pq) != 1:
            
            for i in range(k-1):
                pq.appendleft(pq.pop())
            
            pq.pop()
        
        return pq.pop()