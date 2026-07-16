class Solution:
    def combinationSum4(self, arr: List[int], a: int) -> int:
        dp=[-1]*(a+1)
        def solve(a):
            if a==0:
                return 1
            if dp[a]!=-1:
                return dp[a]
            res=0
            for x in arr:
                if a-x>=0:
                    res+=solve(a-x)
            dp[a]=res
            return dp[a]
        return solve(a)

