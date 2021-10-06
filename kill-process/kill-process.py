class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        map = defaultdict(list)
        
        
        for i in range(len(pid)):
            map[ppid[i]].append(pid[i])
        
        print(map)
        seen = set()
        
        q = [kill]
        seen.add(kill)
        
        while q:
            
            data = q.pop(0)
            
            if data in map:
                for nei in map[data]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
             
            else:
                seen.add(data)
                
           
        print(seen)
        
        return list(seen)
        