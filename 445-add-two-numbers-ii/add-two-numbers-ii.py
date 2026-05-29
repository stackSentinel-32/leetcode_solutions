# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prev_node=None
        curr_node=l1
        while curr_node!=None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node

        l1=prev_node

        prev_node=None
        curr_node=l2
        while curr_node!=None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node

        l2=prev_node

        currl1=l1
        currl2=l2

        dummy=ListNode(0)
        temp=dummy
        carry=0

        while currl1!=None or currl2!=None or carry:

            x=currl1.val if currl1 else 0
            y=currl2.val if currl2 else 0

            total =x+y+carry
            carry=total//10

            temp.next=ListNode(total%10)
            temp=temp.next

            if currl1!=None:
                currl1=currl1.next

            if currl2!=None:
                currl2=currl2.next

        prev_node=None
        curr_node=dummy.next

        while curr_node != None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node

        return prev_node