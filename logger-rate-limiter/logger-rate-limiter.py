class Logger:

    def __init__(self):
        
        self.map = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        map = self.map
        
        if message not in map:
            map[message] = timestamp
            
            return True
        else:
            
            #get val 
            val = map[message]
            
            logic = val + 10 <= timestamp
            
            if logic:
                map[message] = timestamp
                return True
            else:
                return False
                
            
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)