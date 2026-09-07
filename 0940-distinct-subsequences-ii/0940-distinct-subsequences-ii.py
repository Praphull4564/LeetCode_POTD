class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        st = {}
        dp = [0] * len(s)

        dp[0] = 1
        st[s[0]] = 0

        for i in range(1, len(s)):
            if s[i] in st:
                j = st[s[i]]
                dp[i] = (2 * dp[i-1] - (dp[j-1] if j > 0 else 0)) % MOD
            else:
                dp[i] = (2 * dp[i-1] + 1) % MOD

            st[s[i]] = i

        return dp[-1]