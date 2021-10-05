"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        map = {}
        
        
        
        def clone(node):
            if node in map:
                return map[node]
            
            
            copy = Node(node.val)
            map[node] = copy
            
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy
        
        return None if not node else clone(node)
        