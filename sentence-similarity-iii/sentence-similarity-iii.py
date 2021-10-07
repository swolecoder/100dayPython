from collections import defaultdict,Counter
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        if len(sentence1) == len(sentence2):
            return sentence1 == sentence2
        sentence1,sentence2 = sentence1.split(" "),sentence2.split(" ")
        a = deque(sentence1)
        b = deque(sentence2)
        print("adsjmocdjadsc",a,b)
        i = 0
        while a and b and a[0] == b[0]:
            print("adsjmocdjadsc")
            a.popleft()
            b.popleft()
        
        while b and a and a[-1] == b[-1]:
            b.pop()
            a.pop()
        
        
        print(a,b)
        
        return not a or not b