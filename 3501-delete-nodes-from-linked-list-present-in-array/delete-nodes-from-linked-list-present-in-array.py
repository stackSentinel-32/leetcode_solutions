# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        dummy=ListNode(0)
        temp=dummy
        curr=head
        while curr!=None:
            if curr.val not in nums:
                temp.next=ListNode(curr.val)
                temp=temp.next
                
            curr=curr.next
        return dummy.next
        