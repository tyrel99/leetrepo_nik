class Solution:
    def countVowelStrings(self, n: int) -> int:
        def helper(n,vowel):
            res = 0
            
            if n == 0 :
                return 1
            
            for i in range(vowel,5):
                res += helper(n-1,i)
            return res
        
        return helper(n,0) 