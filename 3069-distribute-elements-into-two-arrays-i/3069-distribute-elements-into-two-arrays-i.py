class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        l1=[nums[0]]
        l2=[nums[1]]
        for i in nums[2:]:
            if l1[-1]>l2[-1]:
                l1.append(i)
            else:
                l2.append(i)
        return l1+l2