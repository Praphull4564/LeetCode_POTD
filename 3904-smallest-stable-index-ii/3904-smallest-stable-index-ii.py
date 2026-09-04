class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mi=[nums[-1]]
        ma=[nums[0]]
        for i in range(len(nums)-1,-1,-1):
            mi.append(min(mi[-1],nums[i]))
        mi=mi[::-1]
        for i in range(1,len(nums)):
            ma.append(max(ma[-1],nums[i]))
        for i in range(len(nums)):
            if ma[i]-mi[i]<=k:
                return i
        return -1