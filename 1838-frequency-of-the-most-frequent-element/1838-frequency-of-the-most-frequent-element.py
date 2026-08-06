class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=1
        pfs=[nums[0]]
        for i in range(1,len(nums)):
            pfs.append(pfs[-1]+nums[i])
        for x in range(1,len(nums)):
            i=0
            j=x-1
            f=1
            while j>=i:
                mid = (i+j)//2
                if mid != 0:
                    ts = pfs[x] - pfs[mid-1]
                else:
                    ts = pfs[x]

                diff = (x-mid+1)*nums[x] - ts
                if diff <= k:
                    f = max(f, x-mid+1)
                    j = mid-1
                else:
                    i = mid+1
            res=max(f,res)
        return res
            