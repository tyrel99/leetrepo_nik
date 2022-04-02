class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def Palindrome(s, i ,j):
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return Palindrome(s,i+1,j) or Palindrome(s,i,j-1)
        return True
        