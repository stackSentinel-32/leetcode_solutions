# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None or head.next==None:
            return head

        if head.next.next==None:
            second=head.next
            second.next=head
            head.next=None
            # head.next.next,head.next=head,None
            head=second
    
            return head

        # first=head
        # second=head.next
        # while first.next.next!= None and second.next!=None:
        #     second.next,first.next=first,second
        #     second=second.next.next
        #     first=first.next

        # return head

        prev=None
        curr=head
        head=head.next

        while curr and curr.next:

            second=curr.next
            front=second.next

            second.next=curr
            curr.next=front

            if prev:
                prev.next=second

            prev=curr
            curr=front

        return head