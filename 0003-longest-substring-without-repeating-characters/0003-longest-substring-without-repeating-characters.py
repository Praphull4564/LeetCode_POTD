class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        st = {}

        for j in range(len(s)):
            if s[j] in st:
                i = max(i, st[s[j]] + 1)

            st[s[j]] = j
            res = max(res, j - i + 1)

        return res