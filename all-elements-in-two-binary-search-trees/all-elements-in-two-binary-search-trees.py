from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inOrder(root,list):
            if not root:
                return None
            inOrder(root.left,list)
            list.append(root.val)
            inOrder(root.right,list)
           
        
        
        self.l1 = deque([])
        self.l2 = deque([])
        
        inOrder(root1,self.l1)
        inOrder(root2,self.l2)
        print(self.l1,self.l2)
        
        ans = []

        while self.l1 and self.l2:

            if self.l1== self.l2:
                ans.append(self.l1.popleft())
                ans.append(self.l2.popleft())
            elif self.l1< self.l2:
                ans.append(self.l1.popleft())
               
            else:
                ans.append(self.l2.popleft())
        
        while self.l1:
            ans.append(self.l1.popleft())

        while self.l2:
            ans.append(self.l2.popleft())
        
        return ans
        
        
        
        
        