class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        s=[i for i in s]

        def rev(i,j):
            n=sum(1 if s[i]!="" else 0 for i in range(i,j))//2
            s[i]=""
            s[j]=""
            i,j=i+1,j-1
            while i<len(s) and s[i]=="":
                    i+=1
            while j>=0 and s[j]=="":
                    j-=1

            for iddc in range(n):
                s[i],s[j]=s[j],s[i]
                i+=1
                while i<len(s) and s[i]=="":
                    i+=1
                j-=1
                while j>=0 and s[j]=="":
                    j-=1

        for i in range(len(s)):
            if s[i]=='(':
                l.append(i)
            elif s[i]==')':
                rev(l.pop(),i)
            else:
                continue

        return "".join(s)

