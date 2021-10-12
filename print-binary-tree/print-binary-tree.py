# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def height(node):
            if not node:
                return -1
            
            return 1 + max(height(node.left),height(node.right))
        h = height(root) 
        row = height(root) +1
        col = 2 ** (row) -1
        
        dp = [ [""] * col for _ in range(row)]
        
        
        def dfs(node, r,col, h):
            if not node:
                return 
            
            dp[r][col] = str(node.val)
        
            if node.left:
                c1 = int(col - 2 ** (h - r -1))
                dfs(node.left, r+1, c1,h)
            if node.right:
                c1 = int(col + 2 ** (h - r -1))
                dfs(node.right, r+1, c1,h)
            
            
        dfs(root,0,col//2, h)   
        
        print(row, col,dp)
        return dp