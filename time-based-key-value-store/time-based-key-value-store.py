class TimeMap:

    def __init__(self):
        
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value,timestamp])
            
        

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        val = self.map.get(key, [])
        
        l , r = 0, len(val)-1
        
        while l <= r:
            
            m = (l +r)//2
            
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m +1
            else:
                r = m-1
        
        
        
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)