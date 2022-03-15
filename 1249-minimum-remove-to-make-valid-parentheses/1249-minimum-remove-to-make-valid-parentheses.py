class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt_open, cnt_close, res = 0, 0, ""
        
        for char in s:
            if char == '(':
                cnt_open += 1
            if char == ')':
                cnt_close += 1
            if cnt_open < cnt_close:
                cnt_close -= 1
            else:
                res = res + char
            
        s = res 
        
        cnt_open, cnt_close, res = 0, 0, ""
        for char in reversed(s):
            if char == '(':
                cnt_open += 1
            if char == ')':
                cnt_close += 1
            if cnt_close < cnt_open:
                cnt_open -= 1
            
            else:
                res = char + res
        return res
        
        