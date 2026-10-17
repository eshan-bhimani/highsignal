class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l <= r:
            sl = s[l]
            sr = s[r]
            if not sl.isalnum():
                l += 1
                continue
            if not sr.isalnum():
                r -= 1
                continue
            
            if sl.lower() != sr.lower():
                return False
            l += 1
            r -= 1
        return True

        