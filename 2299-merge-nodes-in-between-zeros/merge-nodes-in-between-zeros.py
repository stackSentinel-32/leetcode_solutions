# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head.next
        dummy = ListNode(0)
        curr = dummy
        
        total = 0
        while temp:
            if temp.val == 0:
                curr.next = ListNode(total)
                curr = curr.next
                total = 0
            
            else:
                total += temp.val
            
            temp = temp.next
        return dummy.next
    
                


