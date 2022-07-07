class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""
        for i,v in enumerate(number):
            if v == digit:
                curr = number[:i]+number[i+1:]
                
                if best == "" or curr > best:
                    best = curr
        return best