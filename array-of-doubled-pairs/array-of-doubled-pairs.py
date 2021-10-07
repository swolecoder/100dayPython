class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        data = sorted(arr, key=lambda item: abs(item))
        
        map = Counter(arr)
        print(data,map)
        
        N = 0
        ans = []
        
        for num in data:
            
            if num == 0 and map[2*num] >=2:
                map[num] -=2
                ans.append(num)
            elif num != 0 and map[num] and map[2*num]:
                ans.append(num)
                map[num] -=1
                map[2*num] -=1
        
        
        print(ans)
        
        return True if len(ans) == len(data)//2 else False