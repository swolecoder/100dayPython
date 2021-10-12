# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        total = 0
        def dfs(node, prev):
            nonlocal total
            if not node:
                return 
            
            prev = max(node.val,prev)
            cal = True if node.val >= prev else False
            
            if cal:
                total +=1
                
            dfs(node.left,prev)
            dfs(node.right,prev)
            
        
        dfs(root, root.val)
        return total       
        