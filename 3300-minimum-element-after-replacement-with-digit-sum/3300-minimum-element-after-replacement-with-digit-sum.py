class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=float("+inf")
        for i in nums:
            n=str(i)
            d=0
            for j in n:
                d+=int(j)

            m=min(m,d)
        return m
            
