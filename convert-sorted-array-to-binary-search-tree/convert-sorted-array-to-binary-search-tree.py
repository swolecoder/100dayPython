# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        def dfs(arr):
            if not arr:
                return None
            
            
            middle = len(arr)//2
            
            node = TreeNode(arr[middle])
            
            node.left = dfs(arr[:middle])
            node.right = dfs(arr[middle+1:])
            
            return node
        
        return dfs(nums)