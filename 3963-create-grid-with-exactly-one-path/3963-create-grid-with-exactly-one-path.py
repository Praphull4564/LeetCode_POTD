class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[['#']*n for i in range(m-1)]
        grid.append(['.']*n)
        for i in range(len(grid)):
            grid[i][0]='.'
            grid[i]="".join(grid[i])
        return grid