# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        minNumber = float('-inf')
        maxNumber = float('inf')
        
        
        def dfs(node, minN, maxN):
            if not node:
                return True
            
            if node.val <= minN or node.val >= maxN:
                return False
            
            left = dfs(node.left, minN, node.val)
            right = dfs(node.right, node.val, maxN)
            
            return left and right
      
        return dfs(root, minNumber, maxNumber)
        
        