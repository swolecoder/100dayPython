from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        q = deque([0])
        
        lookup = set(wordDict)
        visit = set()
        while q:
            
            index = q.popleft()
            
            if index in visit:
                continue
            
            for i in range(index, len(s)+1):
                end = i+1
                newWord = s[index:end]
                if newWord in lookup:
                    q.append(i+1)
                    
                    if end == len(s):
                        return True 
                    visit.add(index)
        return False