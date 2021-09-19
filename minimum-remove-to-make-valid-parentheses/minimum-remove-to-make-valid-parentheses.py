class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        data = list(s)
        
        open = 0
        
        for i in range(len(data)):
            curr = data[i]
            
            if curr == "(":
                open +=1
            elif curr == ")":
                if not open:
                    data[i] = "#"
                else:
                    open -=1
        
        open = 0
        for i in range(len(data)-1,-1,-1):
            curr = data[i]
            
            if curr == ")":
                open +=1
            elif curr == "(":
                if not open:
                    data[i] = "#"
                else:
                    open -=1
        print(data)
        
        def filterhelper(s):
            return s[0] != "#"
        a = filter(filterhelper, data)
        # print(''.join(a))
        return ''.join(a)