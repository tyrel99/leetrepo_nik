class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(large):
            subarr = 0
            currsum = 0
            
            for n in nums:
                currsum += n
                if currsum > large:
                    subarr += 1
                    currsum = n
            return subarr + 1 <= m
        
        l,r = max(nums), sum(nums)
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res