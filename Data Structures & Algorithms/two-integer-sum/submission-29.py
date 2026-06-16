class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, key in enumerate(nums):
            diff = target - key
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[key] = index

        