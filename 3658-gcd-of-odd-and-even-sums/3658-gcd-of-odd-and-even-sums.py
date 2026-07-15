import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        s1,s2=0,0

        for i in range(1,2*n+1):
            if i%2==1:
                s1+=i
            else:
                s2+=i

        return math.gcd(s1,s2)

        
