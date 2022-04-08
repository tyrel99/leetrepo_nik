class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = target - nums[i]
                if s == nums[j]:
                    res.append(i)
                    res.append(j)
        return res
                    
       
            
        
        
        