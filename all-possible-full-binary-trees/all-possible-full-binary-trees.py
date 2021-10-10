# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        
        map = {}
        
        def dfs(n):
            
            if n == 0:
                return []
            
            if n == 1:
                return [TreeNode()]
            
            if n in map:
                return map[n]
            res = []
            for l in range(0,n): # 0 --> n -1
                
                r = n-l-1
                
                left, right = dfs(l), dfs(r)
                
                for leftchild in left:
                    for rightChild in right:
                        res.append(TreeNode(0,leftchild,rightChild))
            
            map[n] = res
            return res
        
        return dfs(n)
        