class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r, l = len(heights) - 1, 0 
        max_area = 0
        while r > l:
            area = min(heights[r], heights[l]) * (r - l)
            max_area = max(max_area, area)

            if heights[r] > heights[l]:
                l += 1
            else :
                r -= 1
        
        return max_area