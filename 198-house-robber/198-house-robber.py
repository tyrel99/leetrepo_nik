class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
    
        def f(ind, nums,dp):
            if ind == 0 : return nums[ind]
            if ind < 0 : return 0
            
            
            if dp[ind] != -1: return dp[ind]
            
            pick = nums[ind] + f(ind-2,nums,dp)
            not_pick = 0 + f(ind-1,nums,dp)
            
            dp[ind] =  max(pick,not_pick)
            return dp[ind]
        
        return f(n-1,nums,dp)
        