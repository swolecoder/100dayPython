class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        data = [[]]
        
        nums.sort()
        
        for i in nums:
            for j in list(data):
                data.append(j + [i])
        
        print(data)
        
        a =  [list(l) for l in set([tuple(l) for l in data])]
        return a