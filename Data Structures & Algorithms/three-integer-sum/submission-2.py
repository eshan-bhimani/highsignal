class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i,n in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                left = nums[l]
                right = nums[r]
                twopointer = left + right
                if n + twopointer > 0:
                    r -= 1
                elif n + twopointer < 0:
                    l += 1
                elif n + twopointer == 0:
                    if [n, left, right] not in result:
                        result.append([n, left, right])
                    l += 1
                    r -= 1
        return result

                    





                
                
        
        


        