# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        
        def dfs(root):
            nonlocal ans
            if not root:
                return False
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            val = root.val == p.val or root.val == q.val
            
            if (l and r) or (l and val) or (r and val):
                ans = root
            
            return l or r or val
        
        dfs(root)
        return ans
        