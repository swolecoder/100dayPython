class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        
        # print(intervals)
        
        a = sorted(intervals, key=lambda interval: interval[0]) 
        
        res = [a[0]]
        
        
        for i in range(1,len(a)):
            prev = res[-1]
            curr= a[i]
            
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(curr)
        
        return res
            
        