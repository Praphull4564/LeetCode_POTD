class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        if all(x==0 for x in nums):
            return 0
        xr=0
        for i in nums:
            xr=xr^i
        if xr!=0:
            return len(nums)
        else:
            return len(nums)-1