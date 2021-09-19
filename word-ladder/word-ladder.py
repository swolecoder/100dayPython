from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        lookup = set(wordList)
        
        
        
        if beginWord == endWord:
            return 0
        
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        level = 0
        
        while q:
            print(level,q)
            for _ in range(len(q)):
                
                currentWord = q.popleft()
                
                if currentWord == endWord:
                    return level +1
                
                for i in range(len(currentWord)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        newWord = currentWord[:i] + j + currentWord[i+1:]
                        
                        if newWord in lookup and newWord not in visited:
                            visited.add(newWord)
                            q.append(newWord)
                
                
                
                
            level +=1
            
            
        return 0  
            
            
            
        
        
        