class Solution:
    def generate(self, n: int) -> List[List[int]]:
        triangle = [[]for _ in range(n)]
        print(triangle)
        
        
        for i in range(n):
            for j in range(0,i+1):
                if j == 0:
                    triangle[i].append(1)
                elif j == i:
                     triangle[i].append(1)
                else:
                     triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        print( triangle)
        
        return  triangle