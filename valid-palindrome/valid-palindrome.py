class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        inputS = list(n.lower() for n in s  if n.isalnum())
        print(inputS)
        
        l = 0
        r = len(inputS)-1
        
        
        while l < r:
            
            if inputS[l] != inputS[r]:
                return False
            l +=1
            r -=1
        
        return True