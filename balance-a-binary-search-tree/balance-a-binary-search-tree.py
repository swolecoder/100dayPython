# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.data = []
        
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.data.append(node.val)
            dfs(node.right)
        dfs(root)
        
        print(self.data)
        
        
        def build(arr):
            if not arr:
                return None
            
            middle = len(arr)//2
            root = TreeNode(arr[middle])
            root.left = build(arr[0:middle])
            root.right = build(arr[middle+1:])
            
            return root
        
        return build(self.data)
        