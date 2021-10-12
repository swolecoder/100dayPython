# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        
        def dfs(root):
            
            if not root:
                #with and  without
                return [0,0]
            
            
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            
            withGivenNode = left[1]+right[1] + root.val
            withoutNode = max(left) + max(right)   #left[0]+right[0]
            
            return [withGivenNode,withoutNode]
        
        a = dfs(root)
        
        print(a)
        
        return max(a[0],a[1])
        