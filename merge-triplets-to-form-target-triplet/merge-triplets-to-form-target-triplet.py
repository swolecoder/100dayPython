class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = []
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            good.append(triplet)
        
        print(good)
        
        seen = set()
        
        for triplet in good:
            
            for i,v in enumerate(triplet):
                if v == target[i]:
                    seen.add(i)
        
        print(seen)
        return len(seen) == 3
                    
                
        