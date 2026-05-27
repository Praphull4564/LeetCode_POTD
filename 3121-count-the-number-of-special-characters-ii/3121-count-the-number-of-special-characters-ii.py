class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st=dict()
        for i in range(len(word)):
            if word[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and word[i] in st:
                continue
            st[word[i]]=i
        res=0
        x=ord('a')-ord('A')
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i in st and chr(ord(i)+x) in st:
                if st[i]>st[chr(ord(i)+x)]:
                    res+=1
        return res

