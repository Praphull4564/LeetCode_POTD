class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=set([i for i in range(min(nums),max(nums)+1)])
        x=set(nums)
        return sorted(list(l - x))