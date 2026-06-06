class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        s=0
        ls=[]
        for i in nums:
            ls.append(s)
            s+=i

        s=0
        rs=[]
        for i in nums[::-1]:
            rs.append(s)
            s+=i
        rs=rs[::-1]
        res=[]
        for i in range(len(nums)):
            res.append(abs(ls[i]-rs[i]))
        return res