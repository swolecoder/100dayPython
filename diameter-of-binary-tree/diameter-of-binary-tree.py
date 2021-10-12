# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def  diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                #diamter and height
                return [-1,-1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            diamter = left[1] + right[1] + 2
            
            res = max(res,diamter)
            height = 1 + max(left[1],right[1])
            print([diamter, height])
            return [diamter, height]
        
        dfs(root)
        
        return res
            
            
#         if not node:
#             return 0
#         l = self.height(node.left)
#         r = self.height(node.right)
#         return max(l,r)+1
        
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         l = self.height(root.left)
#         r = self.height(root.right)
#         lDiameter = self.diameterOfBinaryTree(root.left)
#         rDiamter = self.diameterOfBinaryTree(root.right)
#         return max(l+r, max(lDiameter,rDiamter))

         
        
    
    
    
    
