class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_Area = 0
        while l <= r:
            
            max_Area = max(max_Area,min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_Area
        
        