class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        n=len(str(bin(len(nums)))[2:])
        return 1<<n