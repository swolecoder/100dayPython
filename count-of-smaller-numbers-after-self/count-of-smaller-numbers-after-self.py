from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        s = SortedList()
        ans = []
        
        for n in nums[::-1]:
            index = SortedList.bisect_left(s,n)
            ans.append(index)
            s.add(n)
        
        print(ans)
        return ans[::-1]
        