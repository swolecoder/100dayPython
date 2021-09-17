from collections import deque
import math
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        l = [0]* len(arr)
        r = [0]* len(arr)
        
        mod = pow(10,9)+7
        
        stack1 = deque([])
        stack2 = deque([])
        
        for i in range(len(arr)):
            
            curr = arr[i]
            
            count = 1
            while stack1 and stack1[-1][0] >= curr:
                d = stack1.pop()
                count += d[1]
            
            l[i] = count
            stack1.append((curr,count))
        
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            count = 1
            
            while stack2 and stack2[-1][0] > curr:
                d = stack2.pop()
                count +=d[1]
            
            r[i]= count
            stack2.append((curr,count))
            
        print(l,r)
        
        ans = 0
        
        for i in range(len(l)):
            ans += arr[i]*l[i] * r[i]
        return ans % mod
        