# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        stack = [(root,1)]
        
        ans = 0
        while stack:
            
            node, level = stack.pop()
            
            ans = max(ans, level)
            
            if node.left:
                stack.append((node.left, level +1 if node.left.val - node.val == 1 else 1))
            if node.right:
                stack.append((node.right, level +1 if node.right.val - node.val == 1 else 1))
        
        return ans