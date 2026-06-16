class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            cLeft = s[left]
            cRight = s[right]

            if not cLeft.isalnum():
                left += 1
                continue
            if not cRight.isalnum():
                right -= 1
                continue
            
            if cLeft.lower() != cRight.lower():
                return False
            
            left += 1
            right -= 1
        return True
        