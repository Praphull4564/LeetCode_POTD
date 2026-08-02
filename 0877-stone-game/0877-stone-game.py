class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp=dict()
        def solve(i,j):
            if i==j:
                return piles[i]
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            px= piles[i]+min(solve(i+2,j),solve(i+1,j-1))
            py= piles[j]+min(solve(i+1,j-1),solve(i,j-2))
            dp[(i,j)]=max(px,py)
            return dp[(i,j)]
        n=solve(0,len(piles)-1)
        return n>sum(piles)-n
