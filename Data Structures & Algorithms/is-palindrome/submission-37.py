class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        while left < right:
            cLeft = s[left]
            cRight = s[right]

            if cLeft.isalnum():
                left += 1
                continue
            if cRight.isalnum():
                right -= 1
                continue
            
            if cLeft.lower() != cRight.lower():
                return False
        
            left +=1
            right -=1
        return True
        