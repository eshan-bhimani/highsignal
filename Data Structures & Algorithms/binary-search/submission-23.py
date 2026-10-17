class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            num = nums[mid]
            if num < target:
                l += 1
                mid = (l + r) // 2
            if num > target:
                r -= 1
                mid = (l + r) // 2
            if num == target:
                return mid
        
        return -1

            
        