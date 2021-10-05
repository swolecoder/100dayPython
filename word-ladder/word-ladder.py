class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        
        map = defaultdict(list)
        for word in wordList:
            
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                map[pattern].append(word)
        
        print(map)
        
        q = deque()
        q.append(beginWord)
        
        res = 0
        visited = set()
        
        while q:
            
            for j in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return res+1
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for nei in map[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            
            res +=1
        return 0