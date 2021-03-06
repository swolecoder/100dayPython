# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            return max(left, right)+1
        
        
        
        if not root:
            return 0
        
        
        left = height(root.left)
        right = height(root.right)
        
        return max(left,right)+1
        