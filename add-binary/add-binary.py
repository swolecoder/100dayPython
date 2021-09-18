class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        ans = ""
        
        a = list(a)
        b = list(b)
        carry = 0
        
        while a or b or carry ==1:
            
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            ans = str(carry % 2) + ans
            
            carry = carry//2
        
        
        return ans
        