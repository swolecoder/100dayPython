class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        O(n) solution with stack
        '''
        N = len(s)
        
        # traverse the string
        toadd = 0
        stack = []
        i = 0
        while i<N:
            if s[i]=='(':
                stack.append(s[i])
                i += 1
            else:
                if not stack:
                    if i+1 < N and s[i+1] == ")":
                        toadd +=1
                        i +=2
                    else:
                        toadd +=2
                        i +=1
                else:
                    if i+1 < N and s[i+1] == ")":
                        
                        i += 2
                    else:
                        toadd += 1
                        i +=1
                        
                    stack.pop()
                    
        # check the length of stack
        if len(stack)>0:
            toadd += len(stack)*2
        
        return toadd