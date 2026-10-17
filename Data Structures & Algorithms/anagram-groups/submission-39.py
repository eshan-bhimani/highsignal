class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        result = []

        for s in strs:
            count = [0] * 26

            for c in s:
                result[tuple(count)] += 1
        return list(result.values())

        