"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        original = head
        
        
        while head:
            
            if head.next.val > head.val:
                if insertVal >= head.val and insertVal <= head.next.val:
                    break
            elif head.next.val < head.val:
                if insertVal >= head.val or insertVal <= head.next.val:
                    break
            elif head.next == original:
                break
            
            head = head.next
        
  
        head.next = Node(insertVal,head.next)
        
        
        return original
            
            
        
        