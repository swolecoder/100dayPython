class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        print(nums)
        
        if len(nums) < 3 or nums[0] > 0:
            return []

        result = []
        visited = set()
        
        for i in range(len(nums)-2):
            j = i +1
            k = len(nums)-1

            while j < k  :
                sum = nums[i] + nums[j]+nums[k]
                
                if sum == 0:
                    key = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if key not in visited:
                        print(i,j,k)
                        result.append([nums[i], nums[j], nums[k]])
                        visited.add(key)
                    j +=1
                    k -=1
                elif sum  > 0:
                    
                    k -=1
                else:
                    j +=1
        return result
                    
                    
        