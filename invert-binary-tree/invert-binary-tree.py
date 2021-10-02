# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return 
        
        head = root
        
        q = [root]
        
        while q:
            
            node = q.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        print(head)
        return head
            
        