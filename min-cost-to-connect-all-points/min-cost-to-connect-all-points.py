from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        map = {i:[] for i in range(N)}
        
        
        for i in range(N):
            x1,y1 = points[i][0], points[i][1]
            
            for j in range(i+1, N):
                x2,y2 = points[j][0], points[j][1]
                
                dist = abs(x2-x1) + abs(y2-y1)
                
                map[i].append([dist,j])
                map[j].append([dist,i])
                
        
        
        heap = [[0,0]]
        
        seen = set()
        
        ans = 0
        
        
        while len(seen) < N:
            
            cost, i = heapq.heappop(heap)
            
            if i in seen:
                continue
            ans += cost
            seen.add(i)
                
            
            for c,nei in map[i]:
                
                if nei not in seen:
                    heapq.heappush(heap,(c,nei))
                    
        
        
        return ans
                    
                
                
                
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
        