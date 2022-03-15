class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for i in path.split('/'):
            if not i or i == ".":
                continue
            
            
            if i and i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        res = '/'
        for i in stack:
            res += i
            res += '/'
            
        return res[:-1]if res !=  '/' else '/'
            
                
       
        