# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    
        # l=[]
        # curr=0
        # while len(l) != (len(list1)+len(list2)+(b-a+1)+1) and curr<len(list1):
        #     if curr<a:
        #         l.append(list1[curr])
            
        #     elif curr == a:
        #         while list2!=[]:
        #             l.append(list2.pop(0))

        #     elif curr > b:
        #         l.append(list1[curr])
            
        #     curr+=1
        # return l

        first=list1
        for i in range(a-1):
            first=first.next
        second=first
        
        for i in range(b-a+2):
            second=second.next
        
        first.next=list2
        
        while list2.next != None:
            list2=list2.next
        
        list2.next=second
        return list1

