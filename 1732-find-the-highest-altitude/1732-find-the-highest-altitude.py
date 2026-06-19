class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        l=[0]
        for i in gain:
            l.append(l[-1]+i)

        return max(l)