from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        map = Counter(target)
        
        print(map)
        
        
        for num in arr:
            
            if num not in map:
                return False
            else:
                map[num] -=1
                
                if map[num] == 0:
                    del map[num] 
        
        return True
        