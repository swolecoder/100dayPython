# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        
        data = deque(preorder)
        
        
        def helper(arr):
            if not arr:
                return None
            
            
            data = arr.popleft()
            
            root = TreeNode(data)
            # l = list(n for n in arr if n < data)
            # print(l,data)
            root.left =  helper(deque(list(n for n in arr if n < data)))
            root.right =  helper(deque(list(n for n in arr if n > data)))
            
            return root
        
        return helper(data)
        