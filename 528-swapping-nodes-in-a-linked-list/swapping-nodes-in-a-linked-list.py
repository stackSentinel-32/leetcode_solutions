# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # n=0
        # curr=head
        # while curr!=None:
        #     n+=1
        #     curr=curr.next
        
        # i=1
        # curr=head

        # first=None
        # second=None

        # while curr:

        #     if i==k:
        #         first=curr

        #     if i==n-k+1:
        #         second=curr

        #     curr=curr.next
        #     i+=1
        
        # if first != None and second !=None :
        #     first.val,second.val = second.val,first.val
        # return head

        n=0
        curr=head
        while curr!=None:
            curr=curr.next
            n+=1
        
        tail=head
        x=n-k
        while x:
            tail=tail.next
            x-=1
        
        curr=head
        while k-1:
            curr=curr.next
            k-=1
        
        curr.val,tail.val=tail.val,curr.val
        return head