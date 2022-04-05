class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_Area = 0
        while l <= r:
            diff = r - l
            max_Area = max(max_Area,min(height[l], height[r]) * diff)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_Area
        
        