class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for i in range(len(s)):
            curr = s[i]
            
            if stack and curr == stack[-1]:
                stack.pop()
            else:
                stack.append(curr)
        return "".join(stack)