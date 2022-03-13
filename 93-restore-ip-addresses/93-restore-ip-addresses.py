class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #check len of s
        res = []
        if len(s) > 12:
            return res
        
        def Backtrack(i, dots, currIP):
            #1st basecase (check if dots == 4 and we reach len of nums)
            if dots == 4 and i == len(s):
                res.append(currIP[:-1])
            
            #2nd basecase (check dots exceed more than 4)
            if dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))): # Loop from i to min(of given condition)
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'): # check if digit is less than equal to 255 and leading 0's are not present
                    
                    Backtrack(j+1, dots + 1, currIP + s[i:j+1] + '.')
            
        Backtrack(0,0,"")
        return res
                
        
        