"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        map = defaultdict(lambda: None)
        
        curr = head
        
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        
        print(map)
        curr = head
        
        while curr:
            dep = map[curr]
            dep.next = map[curr.next]
            dep.random = map[curr.random]
            
            curr = curr.next
        
        return map[head]