class Solution:
    def longestPalindrome(self, s: str) -> str:
        los=[i for i in s]
        s="#"+"#".join(los)+"#"
        c=0
        l=(s[0],1)
        while c!=len(s)-1:
            ss=s[c]
            ls=1
            i=c-1
            j=c+1
            while s[i]==s[j]:
                ss=s[i]+ss+s[j]
                ls+=2
                i=i-1
                j=j+1
                if i<0 or j>len(s)-1:
                    if ls>l[1]:
                        l=(ss,ls)
                    break
            else:
                if ls>l[1]:
                    l=(ss,ls)
            c+=1
        res=""
        for i in l[0]:
            if i!='#':
                res+=i
        return res
        
            


