class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        peoples = sorted(people, key = lambda x: (-x[0], x[1]))
        print(peoples)
        
        ans = []
        
        for (h,k) in peoples:
            ans.insert(k,[h,k])
            
        return ans