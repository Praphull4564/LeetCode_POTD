# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        arr=[]
        nds=[]
        res=head
        while head:
            arr.append(head.val)
            nds.append(head)
            head=head.next
        arr=arr[:left-1]+arr[left-1:right][::-1]+arr[right:]
        for i,j in zip(nds,arr):
            i.val=j
        return res
