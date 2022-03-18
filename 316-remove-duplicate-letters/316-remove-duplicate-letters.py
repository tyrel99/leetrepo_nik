class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        stack = []
        
        for i in range(len(s)):
            last[s[i]] = i
            
            
        for i in range(len(s)):
            if s[i] not in stack:
                while stack and stack[-1] > s[i] and last[stack[-1]] > i:
                    stack.pop()
                    
                stack.append(s[i])
                
        return ''.join(stack)
            
            
       