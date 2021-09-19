class Solution:
    def minSwaps(self, s: str) -> int:
        mismatch = 0
        
        for i in range(len(s)):
            if s[i] == "[":
                mismatch +=1
            else:
                if mismatch:
                    mismatch -=1
        return (mismatch +1 ) //2
