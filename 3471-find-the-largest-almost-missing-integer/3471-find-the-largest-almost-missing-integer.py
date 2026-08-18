class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            d[i]=0
        for i in range(len(nums)-k+1):
            l=nums[i:k+i]
            st=set(l)
            for j in st:
                d[j]+=1
        
        val=set(list(d.values()))
        if 1 not in val:
            return -1
        else:
            res=float('-inf')
            for i in d:
                if d[i]==1:
                    res=max(res,i)
        return res