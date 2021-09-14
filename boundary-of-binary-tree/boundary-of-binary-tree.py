# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        left = []
        
        def isLeaf(root):
            return not root.left and not root.right
        
        def leftF(root):
            if not root or isLeaf(root):
                return None
            
            left.append(root.val)
            
            if root.left:
                leftF(root.left)
            
            elif root.right:
                leftF(root.right)
        
        leaf = []
        def leafF(root):
            if not root:
                return
            
            if isLeaf(root):
                leaf.append(root.val)
            
            leafF(root.left)
            leafF(root.right)
        
        
        
        right = []
        
        def rightF(root):
            if not root or isLeaf(root):
                return
            
            if root.right:
                rightF(root.right)
            elif root.left:
                rightF(root.left)
            
            right.append(root.val)
            
            
        leftF(root.left)
        leafF(root.left)
        leafF(root.right)
        rightF(root.right)
        
        print(left,leaf, right)
        ans = [root.val] + left + leaf + right
        
        return ans