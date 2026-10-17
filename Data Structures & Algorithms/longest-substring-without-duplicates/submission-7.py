class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 1, 2
        left, right = s[l], s[r]
        window = r - l
        for i in range(len(s)):
            left, right = s[l], s[r]
            long = s[l:r + 1]
            if len(set(long)) != len(long):
                l += 1
            else:
                r += 1
            window = max(window, r - l)
        

        return window
