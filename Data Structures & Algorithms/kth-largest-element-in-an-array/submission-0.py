class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort(reverse = True)
        result = len(nums)
        for i in range(result):
            if i + 1 == k:
                return nums[i]
