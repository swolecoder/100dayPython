class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a,b,c = len(s1), len(s2) , len(s3)
        
        if a +b != c:
            return False
        map = {}
        def dfs(i,j,k):
            
            if i == a and j == b and k == c:
                return True
            if (i,j,k) in map:
                return map[(i,j,k)]
            
            b1, b2 = False, False
            
            if i < a and s1[i] == s3[k]:
                b1 = dfs(i+1,j , k+1)
                
            if j < b and s2[j] == s3[k]:
                b2 = dfs(i,j+1, k+1)
            map[(i,j,k)] = b1 or b2    
            return b1 or b2
        
        return dfs(0,0,0)