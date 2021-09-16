# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        map = defaultdict(list)
        
        queue = deque([(root,0)])
        
        while queue:
            n , num = queue.popleft()
            
            if n is not None:
                map[num].append(n.val)
                
                queue.append((n.left,num-1))
                queue.append((n.right,num+1))
        
        print(map)
        
        return [ map[x] for x in sorted(map.keys())]
        