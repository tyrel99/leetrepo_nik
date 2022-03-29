class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashh = {}
        
        for i in range(len(nums)):
            if nums[i] in hashh:
                return nums[i]
            else:
                hashh[nums[i]] = 1
        