class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp=[0]*(max(nums)+1)
        m=max(nums)
        for i in nums:
            dp[i]+=i

        memo=[-1]*(m+1)
        def solve(i):
            if i>m:
                return 0

            if memo[i]!=-1:
                return memo[i]

            s1=dp[i]+solve(i+2)
            s2=solve(i+1)

            memo[i]=max(s1,s2)
            return memo[i]


        return solve(1)























        # n=len(nums)
        # def solve(i,st: set[int]):
        #     if i==n:
        #         return 0
        #     if nums[i] in st:
        #         s=solve(i+1,st)
        #         return s
        #     else:
        #         s1=nums[i]+solve(i+1,st | set([nums[i]-1,nums[i]+1]))
        #         s2=solve(i+1,st)
        #     return max(s1,s2)
        # return solve(0,set())

