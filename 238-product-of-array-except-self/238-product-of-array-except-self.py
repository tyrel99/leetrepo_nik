class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        ans = []
        
        
        for i in range(len(nums)):
            ans.append(left)
            left *= nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
            
        return ans    
        