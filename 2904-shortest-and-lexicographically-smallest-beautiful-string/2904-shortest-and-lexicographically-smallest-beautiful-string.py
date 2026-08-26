class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        from collections import deque
        arr=deque()
        res=float('inf')
        ans=""
        for i in range(len(s)):
            if s[i]=='1':
                arr.append(i) 
            if len(arr)==k:
                if res>=arr[-1]-arr[0]+1:
                    res=arr[-1]-arr[0]+1
                    ans=min(ans,s[arr[0]:arr[-1]+1]) if ans!='' and len(ans)==res else s[arr[0]:arr[-1]+1]
                arr.popleft()
        return ans
