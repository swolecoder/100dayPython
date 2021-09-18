class Solution:
    def calculate(self, s: str) -> int:
        self.stack = []
        num = 0
        sign = "+"
        
        def to_stack(num,sign):
            if sign == "+":
                self.stack.append(num)
            elif sign == "-":
                self.stack.append(-1*num)
            elif sign == "*":
                self.stack.append(self.stack.pop() * num)
            elif sign == "/":
                self.stack.append( int(self.stack.pop()/num))
        
        
        s += "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in {"+", "-","/","*"}:
                to_stack(num,sign)
                num = 0
                sign = s[i]
        
        return sum(self.stack)
            