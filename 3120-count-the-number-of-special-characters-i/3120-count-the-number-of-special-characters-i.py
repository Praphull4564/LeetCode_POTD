class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        st=set()
        for i in word:
            st.add(i)
        res=0
        x=ord('a')-ord('A')
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i in st and (chr(ord(i)+x)) in st:
                res+=1
        return res

