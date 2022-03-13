class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for char in s:
            if char in dictt:
                stack.append(char)
                
            else:
                if len(stack) == 0 or dictt[stack.pop()] != char:
                    return False
        return len(stack) == 0
        