class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split("/")
        
        
        for i in range(len(path)):
            curr = path[i]
            
            if stack and path[i] =="..":
                stack.pop()
            elif curr == "." or curr == "":
                continue
            elif not stack and path[i] =="..":
                continue
            else:
                stack.append(curr)
        
        print(stack)
        
        return "/" + "/".join(stack)