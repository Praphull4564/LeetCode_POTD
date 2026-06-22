class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        l=dict()
        for i in 'balon':
            l[i]=0
        for i in text:
            if i in 'balon':
                l[i]+=1
        cnt=0
        r=True
        while r:
            for i in 'balloon':
                l[i]-=1
                if l[i]<0:
                    r=False
                    break
            else:
                cnt+=1
        return cnt
