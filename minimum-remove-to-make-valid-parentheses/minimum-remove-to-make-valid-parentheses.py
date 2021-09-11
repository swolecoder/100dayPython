class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        data = list(s)
        # print(data, 0 > 0)
        
        count = 0
        
        for i, ch in enumerate(data):
            
            if ch == "(":
                count +=1
            elif ch == ")":
                if count > 0:
                    count -=1
                else:
                    data[i] = "#"
        
        print(data)
        
        
        count = 0
        
        for i in range(len(data)-1,-1,-1):
            if data[i] == ")":
                count +=1
            elif data[i] == "(":
                if count > 0:
                    count -=1
                else:
                    data[i] = "#"
            print(data[i],count)
        
        
        ans = ""
        
        for i, ch in enumerate(data):
            
            if ch not in "#":
                ans += ch
                
        return ans
            
        