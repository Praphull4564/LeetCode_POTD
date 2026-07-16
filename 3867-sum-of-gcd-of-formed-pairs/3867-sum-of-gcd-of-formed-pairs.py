class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        from math import gcd
        mx=nums[0]
        pgcd=[nums[0]]
        for i in range(1,len(nums)):
            mx=max(mx,nums[i])
            pgcd.append(gcd(mx,nums[i]))
        pgcd.sort()
        i=0
        j=len(pgcd)-1
        res=0
        while i<j:
            res+=(gcd(pgcd[i],pgcd[j]))
            i+=1
            j-=1

        return res


        