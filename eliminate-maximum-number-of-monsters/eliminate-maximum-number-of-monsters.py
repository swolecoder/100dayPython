class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time = [0] * len(dist)
        
        for i in range(len(dist)):
            
            time[i] = math.ceil(dist[i]/speed[i])
        
        
        res = 0
        
        time.sort()
        print(time)
        
        for m in range(len(time)):
            
            if m >= time[m]:
                return res
            
            res +=1
        
        return res
        