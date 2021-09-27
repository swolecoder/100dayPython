class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
        }
        
        stack = []
        
        for i in range(len(tokens)):
            curr = tokens[i]
            
            if curr in operator:
                a,b = stack.pop(), stack.pop()
                calculator = operator[curr]
                stack.append(calculator(b,a))
            else:
                stack.append(int(curr))
        
        print(stack)
        
        return stack[-1]
                