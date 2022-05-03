class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        prev = nums[0]
        end = 0
        
        #find the largest index in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]
                
        start = len(nums)-1
        prev = start
        
        for i in range(len(nums)-1,-1,-1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        
        if end != 0:
            return end - start + 1
        else:
            return 0
        
        
        
        