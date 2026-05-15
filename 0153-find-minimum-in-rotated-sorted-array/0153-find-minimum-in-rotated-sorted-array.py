class Solution:
    def findMin(self, nums: List[int]) -> int:
        tc = sorted(nums)
        return tc[0]

        