class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sr=s[::-1]
        n=len(s)
        dp=[[0]*(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==sr[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]