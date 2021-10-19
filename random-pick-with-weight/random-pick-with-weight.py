class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        self.total = 0
        
        for weight in w:
            self.total += weight
            self.weights.append(self.total)
        
        
        

    def pickIndex(self) -> int:
        
        ran = random.randint(1,self.total)
        
        for index,weigt in enumerate(self.weights):
            if ran <= weigt:
                return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()