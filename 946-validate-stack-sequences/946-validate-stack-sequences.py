class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        puI, poI = 0, 0
        
        while puI < len(pushed) and poI < len(popped):
            stack.append(pushed[puI])
            puI += 1
            
            while stack and stack[-1] == popped[poI]:
                stack.pop()
                poI += 1
        return len(stack) == 0
            
        