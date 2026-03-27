# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        conn=head.next

        odd=head
        even=head.next

        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        
        odd.next=conn
        return head
            