class Solution:
    def isValid(self, s: str) -> bool:
        
        map = {
            "{":"}",
            "[":"]",
            "(":")",  
        }
        
        stack = []
        
        for i in range(len(s)):
            
            curr = s[i]
            
            if curr in map:
                stack.append(curr)
            else:
                if stack:
                    
                    lastData= stack.pop()
                    print("Ashish",lastData,map[lastData], curr)
                    if map[lastData] != curr:
                        return False
                else:
                    return False
        
        print(stack)
        
        return (True if not stack else False)
        