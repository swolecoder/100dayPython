class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        print(start)
        
        count = 0
        res = 0
        
        s,e = 0,0
        
        while s < len(start):
            if start[s] < end[e]:
                s +=1
                count +=1
                
            else:
                count -=1
                e +=1
            res = max(res, count)
        
        
        return res 
        