class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        map = Counter(nums)
        print(map)
        
        data = sorted(map.items(), key= lambda item : (item[1],-item[0]))
        print(data)
        ans = []
        for k, v in data:
            
            data = [k for i in range(v)]
            ans = ans + data
            
        return ans