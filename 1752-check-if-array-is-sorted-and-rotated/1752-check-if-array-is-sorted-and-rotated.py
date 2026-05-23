class Solution:
    def check(self, nums: List[int]) -> bool:
        n=''
        for i in nums:
            n+=str(i)+'#'
        n=n+n
        nums.sort()
        sn=''
        for i in nums:
            sn+=str(i)+"#"

        print(n,sn)
        return sn in n