from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = defaultdict(int)
        
        for i in range(len(s)):
            map[s[i]] = i
        
        print(map)
        
        prev = -1
        res = []
        maxRange = -1
        
        for i in range(len(s)):
            maxRange = max(maxRange, map[s[i]])
            
            if maxRange == i:
                print(maxRange,i)
                res.append(i -prev)
                
                prev = i 
                maxRange = 0
        
        print(res)
        return res
                