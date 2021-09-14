"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        map = {}
        
        while p:
            map[p] = p
            p = p.parent
        
        
        while q:
            if q in map:
                return map[q]
            
            q = q.parent
            
        