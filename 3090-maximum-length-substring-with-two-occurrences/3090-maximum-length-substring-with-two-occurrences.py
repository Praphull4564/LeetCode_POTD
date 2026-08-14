class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res=float('-inf')
        for i in range(len(s)):
            d={s[i]:1}
            for j in range(i+1,len(s)):
                if s[j] in d:
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                if d[s[j]]==3:
                    res=max(res,j-i)
                    break
            else:
                res = max(res,len(s)-i)
        return res

                

