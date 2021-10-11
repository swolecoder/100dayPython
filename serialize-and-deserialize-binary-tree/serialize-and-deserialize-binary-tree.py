# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        data = []
        
        def dfs(node):
            if not node:
                data.append("#")
                return 
            
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)    
        print(','.join(data))    
        return ','.join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        
        def dfs(arr):
            if len(arr) == 0:
                return 
            
            
            if arr[0] == "#":
                arr.pop(0)
                return 
            
            node = arr.pop(0)
            node = TreeNode(int(node))
            node.left = dfs(arr)
            node.right = dfs(arr)
            
            return node
            
            
            
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))