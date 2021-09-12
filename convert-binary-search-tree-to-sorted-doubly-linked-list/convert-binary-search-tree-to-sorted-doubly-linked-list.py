"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        def dfs(root):

            nonlocal prev, head
            if not root:
                return None
            
            dfs(root.left)
            print("I am here",root.val)
            #process
            if prev is None:
                newNode = Node(root.val)
                prev = newNode
                head = newNode
            else:
                
                print("I am here")
                newNode = Node(root.val)
                newNode.left = prev
                prev.right = newNode
                
                prev = newNode
       
            dfs(root.right)
        
        
        head = None
        prev = None
        dfs(root)
        

            
        prev.right = head
        head.left = prev
        
        return head