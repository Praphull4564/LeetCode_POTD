class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        ps1=set()

        for i in arr1:
            x=''
            for j in str(i):
                x+=j
                ps1.add(x)


        ps2=set()
        for i in arr2:
            x=''
            for j in str(i):
                x+=j
                ps2.add(x)

        res=0
        for i in ps1:
            if i in ps2:
                res=max(res,len(i))
        return res