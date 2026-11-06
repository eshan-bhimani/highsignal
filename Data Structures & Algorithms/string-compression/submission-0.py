class Solution:
    def compress(self, chars: List[str]) -> int:

        lenchars = len(chars)

        i = 0
        j = 0

        while i < lenchars:
            count = 1

            while i < lenchars - 1 and chars[i] == chars[i + 1]:
                i += 1
                count += 1
            chars[j] = chars[i]
            j += 1

            if count > 1:
                for val in str(count):
                    chars[j] = val
                    j += 1
            i += 1
        return j
        
        