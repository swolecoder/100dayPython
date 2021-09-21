class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def operation(a,b,ops):
            if ops == "+":
                return a +b
            elif ops == "-":
                return a - b
            else:
                return a * b
        
        def helper(data):
            
            if data.isdigit():
                return [data]
            res = []
            
            
            for k in range(len(data)):
                if data[k] in "+-*":
                    left = helper(data[0:k])
                    right = helper(data[k+1:])
                    print(left, right)
                    for i in left:
                        for j in right:
                            res.append(operation(int(i) ,int(j) , data[k]))
                            
            return res
        return helper(expression)
        