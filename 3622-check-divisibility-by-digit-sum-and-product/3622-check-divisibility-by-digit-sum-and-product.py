class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p=1
        s=0
        for i in str(n):
            p*=int(i)
            s+=int(i)
        return n%(p+s)==0