class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                skipi, skipj = s[i+1:j+1], s[i:j]
                return (skipi == skipi[::-1] or skipj == skipj[::-1])
                i += 1
                j -= 1
        return True