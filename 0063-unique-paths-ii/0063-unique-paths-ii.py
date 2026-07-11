class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        m,n=len(grid),len(grid[0])
        dp=[[-1]*n for i in range(m)]
        def solve(i,j):
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if grid[i][j]==1:
                return 0
            else:
                if i+1==m:
                    dp[i][j]=solve(i,j+1)
                elif j+1==n:
                    dp[i][j]=solve(i+1,j)
                else:
                    dp[i][j]=solve(i+1,j)+solve(i,j+1)
            return dp[i][j]
        return solve(0,0)

        