class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        data = ([a,b] for a, b in zip(position,speed))
        print(data)
        
        sortedData = sorted(data, key= lambda item: item[0])
        print(sortedData)
        
        stack = []
        for i in range(len(sortedData)-1,-1,-1):
            timeTarget = (target - sortedData[i][0]) / sortedData[i][1]
            stack.append(timeTarget)
            if stack and len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)