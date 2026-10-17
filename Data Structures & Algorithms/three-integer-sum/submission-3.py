class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i,n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                left, right = nums[l], nums[r]
                pointerSum = left + right
                if pointerSum + n < 0:
                    l += 1
                elif pointerSum + n > 0:
                    r -= 1

                elif pointerSum + n == 0:
                    if [n, left, right] not in res:
                        res.append([n, left, right])
                    l += 1
                    r -= 1
        
        return res
        