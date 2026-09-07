class Solution:
    def distinctSubseqII(self, s: str) -> int:
        st = {}
        dp = [0] * len(s)
        dp[0] = 1
        st[s[0]] = 0

        for i in range(1, len(s)):
            if s[i] in st:
                dp[i] = (2 * dp[i-1] - dp[st[s[i]]-1]) % (10**9 + 7)
                st[s[i]] = i
            else:
                dp[i] = (2 * dp[i-1] + 1) % (10**9 + 7)
                st[s[i]] = i

        return dp[-1]