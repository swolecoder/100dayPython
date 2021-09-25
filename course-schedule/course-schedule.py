from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegres = [0] * numCourses
        m = defaultdict(list)
        
        for i in range(len(prerequisites)):
            a, b = prerequisites[i][0],prerequisites[i][1]
            m[b].append(a)
            indegres[a] +=1
        
        s = deque([])
        
        for i in range(len(indegres)):
            if indegres[i] == 0:
                s.append(i)
                
        res = []
        print(s, m)
        while s:
            data = s.popleft()
            res.append(data)
            
            if data in m:
                for child in m[data]:
                    print("Ass", child,indegres[child] )
                    indegres[child] -=1
                    
                    if indegres[child] == 0:
                        s.append(child)
        
        print(res)
        
        if len(res) == numCourses:
            return True
        
        return False
                    
            
        

        
        
         
        