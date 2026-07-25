class Solution:
    def maxProduct(self, n: int) -> int:
        
        arr=[int(i) for i in str(n)]
        arr.sort()

        return arr[-1]*arr[-2]