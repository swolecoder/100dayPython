# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node):
        if not node:
            return 0
        l = self.height(node.left)
        r = self.height(node.right)
        return max(l,r)+1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)
        lDiameter = self.diameterOfBinaryTree(root.left)
        rDiamter = self.diameterOfBinaryTree(root.right)
        return max(l+r, max(lDiameter,rDiamter))
        
    
    
    
    
