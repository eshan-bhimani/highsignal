class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        left, right = nums[l], nums[r]

        if left < right:
            return left

       
        while l < r:
            m = (l + r) // 2
            mid = nums[m]                
            if mid > right:
                l = m + 1
            else:
                r = m
        
        return nums[l]

