class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return set(len(nums)) < len(nums)
        