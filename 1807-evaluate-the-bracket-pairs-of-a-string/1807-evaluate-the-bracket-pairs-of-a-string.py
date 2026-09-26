class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k={}
        for [i,j] in knowledge:
            k[i]=j

        idx1=[]
        idx2=[]
        for i in range(len(s)):
            if s[i]=='(':
                idx1.append(i)
            if s[i]==')':
                idx2.append(i)

        chg=[]
        for i in range(len(idx1)):
            x=s[(idx1[i]+1):(idx2[i])]
            chg.append(k[x] if x in k else '?' )
        
        l=[i for i in s]

        res=''
        idx=0
        inb=0
        for i in s:
            if i!='(' and inb==0:
                res+=i
            elif inb==1 and i!=')':
                continue
            elif i=='(':
                res+=chg[idx]
                idx+=1
                inb=1
            elif i==')':
                inb=0
        return res






