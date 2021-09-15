class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for i in range(len(s)):
            curr = s[i]
            
            if len(stack) and stack[len(stack)-1] == curr:
                stack.pop()
            else:
                stack.append(curr)
        print(stack)
        return "".join(stack)