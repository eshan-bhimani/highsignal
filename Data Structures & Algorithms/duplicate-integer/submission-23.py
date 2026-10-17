class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums.dict()) < len(nums)
        
        