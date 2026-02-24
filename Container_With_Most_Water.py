class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        left , right = 0 , n - 1
        while left < right:
            width = right - left
            max_h = min(height[left], height[right])
            max_area = max(max_area, max_h * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


