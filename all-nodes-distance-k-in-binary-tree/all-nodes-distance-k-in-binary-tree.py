# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        map = {}
        
        def dfs(node,parent):
            if not node:
                return None
            if node.val not in map:
                map[node.val] = parent
            
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        
        dfs(root, None)
        
        # print(map)
        
        visited = set()
        
        q = [(target, 0)]
        
        ans = []
        while q:
            
            node, level = q.pop(0)
            
            
            if node in visited:
                continue
                
            if node and level == k:
                ans.append(node.val)
                
            visited.add(node)
            
            if node and node.left:
                q.append((node.left, level +1))
            if node and node.right:
                q.append((node.right, level +1))
            # print("dsada", node.val)
            if node and node.val in map:
                print("ashish")
                q.append((map[node.val], level +1))
            
            
        print(ans)   
        return ans    
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        