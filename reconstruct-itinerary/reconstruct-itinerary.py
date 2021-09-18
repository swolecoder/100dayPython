class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        dict = {}
        
        for i in range(len(tickets)):
            print(tickets[i][0])
            d1 = tickets[i][0]
            d2 = tickets[i][1]
            
            if d1 not in dict:
                dict[d1] =[]
            if d2 not in dict:
                dict[d2] = []
            
            dict[d1].append(d2) 
        for k in dict.values():
            print(k)
            k.sort()
        
        self.ans = []
        
        def dfs(node):
            destL = dict[node]
            
            while destL:
                nextD = destL.pop(0)
                dfs(nextD)
            self.ans.append(node)
            
        dfs("JFK")    
            
            
            
        return reversed(self.ans)
        