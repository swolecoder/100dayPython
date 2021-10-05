from heapq import heapify, heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        map = defaultdict(list)
        
        for u,v,w in times:
            map[u].append((v,w))
            
        heap = [(0,k)]
        heapify(heap)
        t = 0
        visited = set()
        while heap:
            w, node = heappop(heap)
            
            if node in visited:
                continue
            t = max(w,t)
            visited.add(node)
            
            for n2, w2 in map[node]:
                if n2 not in visited:
                    heappush(heap,(w2+w, n2))
            
        return t if len(visited) == n else -1
        
        
        