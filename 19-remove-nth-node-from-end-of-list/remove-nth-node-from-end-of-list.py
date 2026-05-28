# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr=head
        # len=0
        # while curr!=None:
        #     len+=1
        #     curr=curr.next

        # if n==len:
        #     head=head.next
        #     return head
        
        # t_node=len-n

        # curr=head
        # idx=1
        # while curr!=None:
        #     if idx==t_node:
        #         break
        #     idx+=1
        #     curr=curr.next
        
        # curr.next=curr.next.next
        # return head



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1=head
        p2=head

        for i in range(n):
            p2=p2.next
        
        if p2==None:
            head=head.next
            return head

        while p2.next!=None:
            p2=p2.next
            p1=p1.next

        p1.next = p1.next.next
        return head
            
