from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.list = deque([])
        self.size = size
        

    def next(self, val: int) -> float:
        self.list.append(val)
        
        if len(self.list) > self.size:
            self.list.popleft()
        
        return sum(self.list) /len(self.list)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)