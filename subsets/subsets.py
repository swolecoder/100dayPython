class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        data = [[]]
        
        for i in nums:
            for j in list(data):
                temp = j + [i]
                data.append(temp)
        return data