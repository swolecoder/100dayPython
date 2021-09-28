# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        if p.right != None:
            curr = p.right
            
            while curr and curr.left:
                curr = curr.left
            
            return curr
        
        succ = None
        
        curr = root
        
        while curr:
            if curr.val > p.val:
                succ = curr
                curr = curr.left
            elif curr.val < p.val:
                curr = curr.right
            else:
                break
        return succ