class Solution:
    def maximumSwap(self, num: int) -> int:
        
        digit = list(map(int, str(num)))
        print(digit)
        m = {}
        
        for i in range(len(digit)):
            m[digit[i]] = i
        
        print(m)
        
        for i in range(len(digit)):
            
            for j in range(9,digit[i],-1):
                index = m.get(j,-1)
                
                if index > i:
                    digit[index], digit[i] = digit[i], digit[index]
                    
                    d = "".join(map(str, digit))

                    return int(d)
                    # ''.join(map(str(int), int))
                    break
        return num
                    
        