from heapq import heapify, heappush, heappop
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if k > len(points):
            return []
        
        heap = []
        heapify(heap)
        
        for a,b in points:
            print(a,b)
            cal = math.pow(a,2) + math.pow(b,2)
            dist = math.sqrt(math.pow(a,2) + math.pow(b,2))
            
            heappush(heap,(dist,[a,b]))
            
        print(heap)
        
        ans = []
        
        while k > 0:
            a,b = heappop(heap)
            print(b)
            k -=1
            ans.append(b)
        
        return ans
        