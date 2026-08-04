class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=[]
        while head:
            x.append(head.val)
            head=head.next
        
        if len(x)==0:
            return head
        x.sort()

        res=ListNode(x[0])
        result=res
        for i in range(1,len(x)):
            res.next = ListNode(x[i])
            res=res.next

        return result