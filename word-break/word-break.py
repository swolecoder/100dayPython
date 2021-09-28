class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(s, lookup):
            
            if not s:
                memo[""] = True
                return True
            if s in memo:
                return memo[s]
            
            for i in range(len(s)):
                newString = s[0: i+1]
                
                if newString in lookup:
                    if dfs(s[i+1:], lookup):
                        memo[s] = True
                        return True
            
            memo[s] = False
            return False
        
        
        lookup = set(wordDict)
        
        return dfs(s, lookup)