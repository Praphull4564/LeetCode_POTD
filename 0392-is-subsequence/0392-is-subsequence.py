class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)==0:
            return True
        i=0
        j=0

        while j<len(t):
            if s[i]==t[j]:
                j+=1
                i+=1
                if i==len(s):
                    return True
            else:
                j+=1

        return False

        