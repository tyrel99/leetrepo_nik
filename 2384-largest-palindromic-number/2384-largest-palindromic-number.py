class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        count = Counter(num)
        
        if len(count) == 1 and count['0'] >= 1:
            return '0'
        
        res1 = ''
        res2 = ''
        mid = -1
        
        for i in range(9,-1,-1):
            while count[str(i)]:
                if not res1 and i == 0:
                    break
                if count[str(i)] >= 2:
                    res1 += str(i)
                    res2 = str(i) + res2
                    count[str(i)] -= 2
                if count[str(i)] == 1:
                    mid = max(mid,i)
                    count[str(i)] -= 1
                if count[str(i)] == 0:
                    del count[str(i)]
                
        return res1 + res2 if mid == -1 else res1 + str(mid) + res2
                    
                    
        
        