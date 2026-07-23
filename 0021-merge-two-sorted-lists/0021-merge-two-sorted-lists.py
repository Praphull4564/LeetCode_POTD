# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        x1=list1
        x2=list2
        while list1:
            l1.append(list1.val)
            list1=list1.next
        while list2:
            l2.append(list2.val)
            list2=list2.next

        if l1==[]:
            return x2
        if l2==[]:
            return x1
        l3=sorted(l1+l2)
        res=ListNode(l3[0])
        curr=res
        for i in range(1,len(l3)):
            curr.next=ListNode(l3[i])
            curr=curr.next
        return res