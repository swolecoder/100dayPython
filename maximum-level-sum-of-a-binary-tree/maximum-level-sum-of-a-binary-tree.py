# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append([root,1])
        ans = float('-inf')
        globalL = 1
        res = 1
        
        
        while q:
            
            l1 = len(q)
            sum  = 0
            for i in range(l1):
                data = q.popleft()
                node = data[0]
                level = data[1]
                globalL = level
                if node:
                    sum += node.val
                
                if node.left:
                    q.append([node.left, level +1])
                if node.right:
                    q.append([node.right, level +1])
                    
            print(sum,globalL)     
            if sum > ans:
                ans = max(ans, sum)
                res = globalL
        
        
        return res
        