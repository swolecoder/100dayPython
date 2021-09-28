class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        if not digits:
            return []
        
        map = {
            "2": "abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        
        def dfs(index, outputstr):
            
            if len(outputstr) == len(digits):
                result.append(outputstr)
                return 
            
            current = map[digits[index]]
            
            for c in current:
                dfs(index+1, outputstr + c)
        
        
        dfs(0,"")
        
        return result