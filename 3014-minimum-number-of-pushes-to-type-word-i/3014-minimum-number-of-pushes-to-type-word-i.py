class Solution:
    def minimumPushes(self, word: str) -> int:
        s=0
        for i in range(len(word)):
            s+=(i//8+1)
        return s