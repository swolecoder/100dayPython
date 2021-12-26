class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        
        q,r = divmod(abs(n),abs(d))
        
        ans = []
        map = {}
        
        if n * d < 0:
            ans.append("-")
        
        ans.append(str(q))
        print(q,r)
        
        if r == 0:
            return ''.join(ans)
        
        ans.append(str("."))
        while r != 0:
            print(map)
            if str(r) in map:
                l = map[str(r)]
                ans.insert(l,"(")
                ans.append(")")
                break
            else:
                map[str(r)] = len(ans)
                
                q1,r1 = divmod(r*10,abs(d))
                print(q1,r1)
                ans.append(str(q1))
                r = r1
        return ''.join(ans)