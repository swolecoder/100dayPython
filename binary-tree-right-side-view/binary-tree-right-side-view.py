# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        q = deque([root])
        
        ans = []
        
        while q:
            level_length = len(q)
            print(level_length)
            for i in range(level_length):
                data = q.popleft()
                if i == level_length-1:
                    ans.append(data.val)
                
                if data.left:
                    q.append(data.left)
                if data.right:
                    q.append(data.right)
        
        
        return ans