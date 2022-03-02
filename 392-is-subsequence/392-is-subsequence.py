class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        remainder  = iter(t)
        
        for char in s:
            if char not in remainder:
                return False
        return True
        