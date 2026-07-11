class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n=len(matrix)

        dp=[[-200]*n for i in range(n)]
        def solve(i,j):
            if i==n-1:
                return matrix[i][j]
            if dp[i][j]!=-200:
                return dp[i][j]
            if j+1==n:
                dp[i][j]=matrix[i][j]+min(solve(i+1,j),solve(i+1,j-1))
            elif j-1<0:
                dp[i][j]=matrix[i][j]+min(solve(i+1,j),solve(i+1,j+1))
            else:
                dp[i][j]=matrix[i][j]+min(solve(i+1,j),solve(i+1,j-1),solve(i+1,j+1))
            return dp[i][j]

        ans=float("inf")
        for i in range(n):
            ans=min(ans,solve(0,i))
        return ans


