from collections import Counter
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        ans = []
        
        items = Counter(arr1+ arr2+arr3)
        
        for a in items:
            # print(k,v)
            if items[a] == 3:
                ans.append(a)
                
        return ans
            
        