class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = 0
        i = 1
        while i < len(nums):
            if nums[res] == nums[i]:
                count += 1
            elif nums[res] != nums[i]:
                count -= 1
            if count == 0:
                count = 1
                res = i
            i += 1
            
        
        count = 0
        for i in range(len(nums)):
            if nums[res] == nums[i]:
                count += 1
                
        if count > len(nums) // 2:
            return nums[res]
            
            
        