class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr = 0
        
        for i in s:
            if i == '(':
                stack.append(curr)
                curr = 0
            else:
                curr = stack.pop() + max(1,curr * 2)
        return curr
       