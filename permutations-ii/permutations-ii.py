class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        def permute(nums):
            if len(nums) == 1:
                return [nums[:]]

            result = []

            prev = -11
            for _ in range(len(nums)):
                num = nums.pop(0)
                if num != prev:
                    perms = permute(nums)
                    for perm in perms:
                        perm.append(num)
                    result.extend(perms)        
                nums.append(num)
                prev = num
            return result
        
        return permute(nums)
        