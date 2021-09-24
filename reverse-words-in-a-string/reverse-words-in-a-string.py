from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
      
        print(s)
        
        i = 0
        r = len(s)-1
        
        while i <= r and s[i] == " ":
            i +=1
        while i <= r and s[r] == " ":
             r -=1
                
        d = deque()
        word = []
        
        while i <=r:
            
            if s[i] == " " and word:
                
                d.appendleft(''.join(word))
                word = []
            elif s[i] != " ":
                word.append(s[i])
            
            i +=1
        d.appendleft(''.join(word))
        print(word)
        
        return ' '.join(d)
         
        