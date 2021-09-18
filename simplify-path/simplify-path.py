class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        # print(path)
        
        stack = []
        
        for i in range(len(path)):
            if path[i] == "..":
                if not stack:
                    continue
                stack.pop()
            elif path[i] == "." or path[i] == "" or path[i] == "/":
                continue
            else:
                stack.append(path[i])
        print(stack)
        
        return "/" + "/".join(stack)