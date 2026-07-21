class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        for i in s:
            if i.isalpha() or i.isdigit():
                x=x+(i.lower())

        n=len(x)//2
        
        for i in range(n):
            if x[i]==x[-(i+1)]:
                continue
            else:
                return False
        
        return True