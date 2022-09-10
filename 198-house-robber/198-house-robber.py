class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        def f(ind,nums,dp):
            for i in range(1,len(nums)):
                take = nums[i]
                if i > 1:
                    take += dp[i-2]
                
                not_take = 0 + dp[i-1]    
                dp[i] = max(take, not_take)
                
        f(0,nums,dp)
        return dp[n-1]
            
        
        