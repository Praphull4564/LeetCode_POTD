class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set()
        for i in nums1:
            s1.add(i)
        s2=set()
        for i in nums2:
            s2.add(i)
        res=list(s1 & s2)
        return min(res) if res else -1
        