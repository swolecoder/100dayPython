class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        lookup = set(wordDict)
        
        q = []
        
        q.append(0)
        
        visited = set()
        while q:
            
            index = q.pop(0)
            if index in visited:
                continue
            
            for i in range(index, len(s)+1):
                newWord = s[index: i+1]
                if newWord in lookup:
                    q.append(i+1)
                    
                    if i +1 == len(s):
                        return True
                    visited.add(index)

        return False