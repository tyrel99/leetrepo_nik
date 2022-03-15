class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new = path.split('/')
        
        for i in new:
            if i == '..':
                stack.pop() if stack else None
            elif i and i != '.':
                stack.append(i)
        
        return "/" + "/".join(stack)
        
        