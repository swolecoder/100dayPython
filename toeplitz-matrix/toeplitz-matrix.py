
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        map = {}
        
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                key = j - i
                
                if key not in map:
                    map[key] = []
                    map[key].append(matrix[i][j])
                else:
                    val = map.get(key)
                    if val[0] != matrix[i][j]:
                        return False
                    else:
                        map[key].append(matrix[i][j])
        return True
                
                
                
        