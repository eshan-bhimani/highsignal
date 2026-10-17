class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        l, r = 0, 0
        window = r - l + 1
        while r < len(s):
            long = s[l:r + 1]
            if len(set(long)) != len(long):
                l += 1
            else:
                r += 1
            window = max(window, r - l)
        

        return window
