class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent
        self.lockStatus = [None] * len(parent)
        self.children = {i:[] for i in range(len(parent))}
        
        for i in range(1,len(parent)):
            self.children[parent[i]].append(i)
        

    def lock(self, num: int, user: int) -> bool:
        if self.lockStatus[num] == None:
            self.lockStatus[num] = user
            return True
        return False
            

    def unlock(self, num: int, user: int) -> bool:
        if self.lockStatus[num] == user:
            self.lockStatus[num] = None
            return True
        return False
            
        
        

    def upgrade(self, num: int, user: int) -> bool:
        
        #It does not have any locked ancestors.
        
        i = num
        
        while i != -1:
            if self.lockStatus[i]:
                return False

            i = self.parent[i]
        
        
        q = deque([num])
        
        
        lock = 0
        while q:
            data = q.popleft()
            if self.lockStatus[data]:
                self.lockStatus[data] = None
                lock +=1

            q.extend(self.children[data])
        
        if lock > 0:
            self.lockStatus[num] = user
        
        return lock > 0
            
                
            
            
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)