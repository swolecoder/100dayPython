from collections import defaultdict, deque
class DSU:
    def __init__(self,p):
        self.p = [i for i in range(p)]
    
    def find(self,x):
        if self.p[x] == x:
            return x
        return self.find(self.p[x])
    
    def union(self,x,y):
        A = self.find(x)
        B = self.find(y)
        
        if A != B:
            self.p[B] = A
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        uf = DSU(len(accounts))
        
        
        # break
        
        emailsToIndex = {}
        indexToName = {}
        
        for i in range(len(accounts)):
            name = accounts[i][:1][0]
            # print(name)
            indexToName[i] = name
            rest = accounts[i][1:]
            
            found = False
            
            for j in range(len(rest)):
                # print(rest[j])
                if rest[j] in emailsToIndex:
                    uf.union(emailsToIndex[rest[j]], i)
                    found = True
                else:
                    emailsToIndex[rest[j]] = i
          
        print(indexToName)
        print(uf.p)
        
        
        ans = defaultdict(list)
        
        for k,v in emailsToIndex.items():
            findParent = uf.find(v)
            ans[findParent].append(k)
        
        
        result = []
        
        for k in sorted(ans.items()):
            temp = [indexToName[k[0]]] + sorted(k[1])
            result.append(temp)
        
        return result
        
        
                    
                    
        