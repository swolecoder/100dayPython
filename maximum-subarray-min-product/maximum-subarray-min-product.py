class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefixSum = [0]
        
        for n in nums:
            prefixSum.append(prefixSum[-1]+n)
        
        
        print(prefixSum)
        
        stack = []
        res = -1
        
        for i in range(len(nums)):
            start = i
            num = nums[i]
            
            #top of stack
            while stack and stack[-1][1] > num:
                index, currentNum = stack.pop()
                print(index, currentNum)
                res = max(res,(prefixSum[i] - prefixSum[index]) * currentNum )
                start = index
            
            
            stack.append((start, num))
        
        print(stack)
        print(res)
        for index, num in stack:
            total = prefixSum[len(nums)] - prefixSum[index]
            print(total, num,total * num)
            res = max(res,total * num)
        
        
        return res % (10**9 + 7) 
        