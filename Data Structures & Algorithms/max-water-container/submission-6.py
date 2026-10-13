class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r, l  = len(heights) - 1, 0
        area = 0
        while r > l:
            area = max(area, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else : 
                r -= 1
        
        return area