class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        countOne = 0
        for d in data:
            if d == 1:
                countOne +=1
        
        print(countOne)
        
        l = 0
        k = countOne
        ans = float("inf")
        currentOne = 0
        
        if k == 0:
            return 0
        for r in range(len(data)):
            if data[r] == 1:
                currentOne +=1
            
            
            # winbdow size is equal k
            if r - l +1 == k:
                print(k,currentOne)
                ans = min(ans,k-currentOne)
                if data[l] == 1:
                    currentOne -=1
                l +=1
            

            
            
        print(ans)
        return ans
                
                
                
                
            
                
            
        