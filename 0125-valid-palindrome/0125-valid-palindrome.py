class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        for i in s:
            if i.isalpha() or i.isdigit():
                x=x+(i.lower())

        i=0
        j=len(x)-1
        
        while i<j:
            if x[i]!=x[j]:
                return False
            else:
                i+=1
                j-=1
        return True