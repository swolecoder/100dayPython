from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # zab -> a, b so the logic for + 26 ZZZ% 26
        
#         map = defaultdict(list)
        
#         for i in range(len(strings)):
#             curr = strings[i]
#             key = ""
#             for j in range(1,len(curr)):
                
#                 key+= str(( (ord(curr[j]) - ord(curr[j-1])) + 26) %26)
            
#             map[key].append(curr)
        
#         return map.values()
        dic = {}
        res = []
        start = ord('a')
        for s in strings:
            prev = ord(s[0])
            key = ""
            for c in s:
                key += chr(start+(prev-ord(c))%26)
            if key not in dic:
                dic[key] = len(res)
                res.append([])
            res[dic[key]].append(s)
        return res
                
        
        