from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        q = deque(['0000'])
        
        graph = {
            '0': ['9','1'],
            '1': ['0','2'],
            '2': ['1','3'],
            '3': ['2','4'],
            '4': ['3','5'],
            '5': ['4','6'],
            '6': ['5','7'],
            '7': ['6','8'],
            '8': ['7','9'],
            '9': ['8','0'],
        }
        
        lookup = set(deadends)
        
        if '0000' in lookup:
            return -1

        index = 0
        while q:
            for _ in range(len(q)):
                data = q.popleft()
                
                if data == target:
                    return index
                
                for i in range(4):
                    for d in graph[data[i]]:
                        newK = data[:i]+ d + data[i+1:]

                        if newK not in lookup:
                            lookup.add(newK)
                            q.append(newK)
            index +=1

        return -1
            
        
        
        