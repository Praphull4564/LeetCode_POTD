# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        if len(arr)<3:
            return [-1,-1]
        fr=[]
        for i in range(1,len(arr)-1):
            if (arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (arr[i]<arr[i-1] and arr[i]<arr[i+1]):
                fr.append(i)
        
        res=[float('inf'),float('-inf')]
        if len(fr)<2:
            return [-1,-1]
        for i in range(1,len(fr)):
            res[0]=min(res[0],fr[i]-fr[i-1])

        return [res[0],fr[-1]-fr[0]]