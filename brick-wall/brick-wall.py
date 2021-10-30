class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        map = Counter()
        map[0] = 0
        for row in wall:
            count = 0
            for b in row[:-1]:
                count += b
                map[count] = 1 + map.get(count,0)
                
            
        maxVal = max(map.values())        
        
        print(map,maxVal)
        
        return len(wall) - maxVal
        