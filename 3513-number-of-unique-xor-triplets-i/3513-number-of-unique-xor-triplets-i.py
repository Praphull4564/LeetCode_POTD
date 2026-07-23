class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        st=set(nums)
        if len(nums)<=2:
            return len(st)
        
        n=len(str(bin(len(nums)))[2:])
        return 1<<n