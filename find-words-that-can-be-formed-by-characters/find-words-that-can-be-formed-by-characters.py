from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        dict = defaultdict(int)
        
        for i in range(len(chars)):
            getVal = dict.get(chars[i],0)
            
            dict[chars[i]] +=1
        
        
        print(dict)
        
        ans = 0
        
        for word in words:
            valid = True
            for c in word:
                if dict[c] >= word.count(c):
                    continue
                else:
                    valid = False
            
            if valid:
                ans += len(word)
                
        
        return ans
            
            
            
        
        
        