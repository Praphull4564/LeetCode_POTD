class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        
        cnts=[]
        c0=1 if s[0]=='0' else 0
        c1=1 if s[0]=='1' else 0
        c=s[0]
        for i in range(1,len(s)):
            if s[i]=='0' and c=='0':
                c0+=1
            elif s[i]=='1' and c=='1':
                c1+=1

            elif s[i]=='0' and c=='1':
                cnts.append((c1,c))
                c1=0
                c0=1
                c='0'
            else:
                cnts.append((c0,c))
                c0=0
                c1=1
                c='1'
        else:
            cnts.append((c1,c) if c1 else (c0,c))

        if len(cnts)<3:
            return s.count('1')

        mc=float('-inf')
        for i in range(1,len(cnts)-1):
            if cnts[i][1]=='1':
                so0=cnts[i-1][0]+cnts[i+1][0]
                mc=max(so0,mc)

        if mc==float('-inf'):
            return s.count('1')
        return s.count('1')+mc





            

            