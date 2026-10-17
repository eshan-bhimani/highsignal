class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 1, len(numbers)

        while l < r:
            left = numbers[l - 1]
            right = numbers[r - 1]

            if left + right < target:
                l += 1
            elif left + right > target:
                r -= 1
            else:
                return [l,r]
