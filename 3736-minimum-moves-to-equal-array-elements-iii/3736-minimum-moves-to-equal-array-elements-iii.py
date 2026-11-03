class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        res=0
        for i in nums:
            res+=(m-i)
        return res