class Solution:
    def maxUncrossedLines(self, text1: List[int], text2: List[int]) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[j-1]==text2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]