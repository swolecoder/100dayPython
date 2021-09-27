class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if len(s) < k:
            return 0
        
        map = Counter(s)
        
        for p, v in enumerate(s):
            
            if map[v] < k:
                
                return max(self.longestSubstring(s[:p],k), self.longestSubstring(s[p+1:], k))
        
        return len(s)