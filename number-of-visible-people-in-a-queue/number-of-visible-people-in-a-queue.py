class Solution:
    def canSeePersonsCount(self, h: List[int]) -> List[int]:
        ans = [0] * len(h)
        
        stack = []
        
        for i in range(len(h)):
            curr = h[i]
            
            while stack and stack[-1][0] < curr:
                data = stack.pop() # h , index
                ans[data[1]] +=1
            
            
            if stack:
                ans[stack[-1][1]] +=1
            
            
            stack.append((curr,i))
        
        
        return ans
                
        