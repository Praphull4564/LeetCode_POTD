class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i,j):
            if i==j:
                return nums[i]
            if i>j:
                return 0
            p1=nums[i]+min(solve(i+2,j),solve(i+1,j-1))
            p2=nums[j]+min(solve(i+1,j-1),solve(i,j-2))
            return max(p1,p2)
        p1=solve(0,len(nums)-1)
        return p1>=(sum(nums)-p1)
            

