class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p=1
        s=0
        m=n//1
        while m!=0:
            x=m%10
            p*=x
            s+=x
            m=m//10
        return n%(p+s)==0