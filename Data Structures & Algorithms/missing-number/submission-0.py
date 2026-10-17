class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i,n in enumerate(nums):
            if i != n:
                return n - 1
        return 0
        