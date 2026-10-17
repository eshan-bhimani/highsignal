class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            left, right = heights[l], heights[r]
            area = min(left, right) * (r - l)
            result = max(area, result)

            if left < right:
                l += 1
            else:
                r -= 1
        
        return result


        