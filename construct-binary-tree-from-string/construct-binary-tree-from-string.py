# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        stack = []
        i = 0
        n = len(s)
        
        while i < n:
            
            if s[i] == "-":
                i +=1
                num = 0 
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i +=1
                
                stack.append(TreeNode(-num))
                i -=1
            elif s[i].isdigit():
                
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i +=1
                
                stack.append(TreeNode(num))
                i -=1
            elif s[i] == ")":
                lastData = stack.pop()
                parent = stack[-1]

                if not parent.left:
                    parent.left = lastData
                else:
                    parent.right = lastData
            
            i +=1
        
        print(stack)
        return stack[0]
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        