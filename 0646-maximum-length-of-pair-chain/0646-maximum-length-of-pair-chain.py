class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()
        n=len(pairs)
        dp=[[-1]*n for i in range(n)]
        def solve(i,j):
            if i>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j!=-1:
                s=0
                if pairs[i][0]>pairs[j][1]:
                    s=1+solve(i+1,i)
                dp[i][j]=max(s,solve(i+1,j))
            else:
                dp[i][j]=1+solve(i+1,i)
                dp[i][j]=max(dp[i][j],solve(i+1,j))

            return dp[i][j]

        return solve(0,-1)
        