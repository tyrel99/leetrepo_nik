class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        if len(nums) < 3:
            return False
        
        second_num = -math.inf
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < second_num:
                return True
            
            while stack and stack[-1] < nums[i]:
                second_num = stack[-1]
                stack.pop()
            
            stack.append(nums[i])
            
        return False
        
        