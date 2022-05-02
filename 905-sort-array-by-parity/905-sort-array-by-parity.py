class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 != 0:
                j -= 1
        return nums
        