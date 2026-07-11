class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp=[[-1]*(len(grid[0])) for i in range(len(grid))]
        def solve(i,j):
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            if i+1==len(grid):
                dp[i][j]=grid[i][j]+solve(i,j+1)
            elif j+1==len(grid[0]):
                dp[i][j]=grid[i][j]+solve(i+1,j)
            else:
                dp[i][j]=min(grid[i][j]+solve(i+1,j),grid[i][j]+solve(i,j+1))


            return dp[i][j]

        return solve(0,0)
            