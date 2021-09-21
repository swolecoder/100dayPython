class Solution:
    def countGoodNumbers(self, p: int) -> int:

        MOD = 10**9 + 7
        even_pos = (p+1)//2
        odd_pos = p//2
        
        even_nums = 5 # 0,2,4,6,8
        prime_nums = 4 # 2,3,4,7
        return (pow(5,even_pos,MOD) * pow(4,odd_pos,MOD)) % MOD
