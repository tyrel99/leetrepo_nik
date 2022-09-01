class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        mid = 0
        r = len(nums)-1
        
        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid],nums[l]
                mid += 1
                l += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[r],nums[mid] = nums[mid],nums[r]
                r -= 1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        