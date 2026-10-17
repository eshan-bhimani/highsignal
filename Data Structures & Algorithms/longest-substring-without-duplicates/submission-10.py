class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        l, r = 0, 1
        left, right = s[l], s[r - 1]
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
