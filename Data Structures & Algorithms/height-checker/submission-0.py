class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        incorrect = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                incorrect += 1
        
        return incorrect