# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return None
            
            
            left = dfs(node.left)
            
            right = dfs(node.right)
            
            
            if node.left:
                left.right = node.right
                node.right = node.left
                node.left = None
                
            balance = right or left or node
            
            return balance
        
        dfs(root)
            
            
            
                
        