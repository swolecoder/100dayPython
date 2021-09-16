class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        sum = ""
        carry = 0
        
        i, j = len(a)-1 ,len(b)-1
        
        
        while i >=0 or j >= 0:
            
            a1 = 0
            b1 = 0
            
            if i >=0:
                a1 = ord(a[i]) - 48
                i -=1
            if j >=0:
                b1 = ord(b[j]) -48
                j -=1
            
            currentSum = a1 + b1 + carry
            
            if currentSum >2:
                sum = "1" + sum
                print("Ashish")
                carry = 1
            elif currentSum == 2:
                sum = "0" + sum
                carry = 1
            elif currentSum == 1:
                sum = "1"+ sum
                carry = 0
            else:
                sum = "0"+sum
                carry = 0
            
            print("ashish",a1,b1, currentSum,carry)
        print(sum, carry)
        
        if carry == 1:
            sum = "1"+ sum
        return sum
                