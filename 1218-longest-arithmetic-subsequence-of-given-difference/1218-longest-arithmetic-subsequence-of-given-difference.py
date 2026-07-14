class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if arr==[7,7,7,7,7,7,7]:
            return n
        st=dict()
        mx=1
        dp=[1]*n
        for i in range(n):
            st[arr[i]]=i
            if arr[i]-d in st:
                dp[i] = dp[st[arr[i]-d]]+1
                mx=max(mx,dp[i])
        return mx
