# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque()
        q.append(root)
        
        ans = []
        
        
        while q:
            length = len(q)
            sum = 0
            for i in range(length):
                node = q.popleft()
                
                if node:
                    sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(sum/length)
        return ans
        
        
        