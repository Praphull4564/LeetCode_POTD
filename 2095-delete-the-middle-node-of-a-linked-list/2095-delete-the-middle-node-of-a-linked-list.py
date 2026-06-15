# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l=[]
        while head:
            l.append(head.val)
            head=head.next

        n=len(l)
        if n%2==0:
            idx=int(n/2)
        else:
            idx=int(n//2)

        l.pop(idx)

        if len(l)>=1:
            hf=ListNode(l[0])
            h=hf
            for i in range(1,len(l)):
                h.next=ListNode(l[i])
                h=h.next
            return hf
        else:
            return 