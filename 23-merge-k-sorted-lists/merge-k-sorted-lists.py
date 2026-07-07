# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(a,b):
            d=ListNode()
            c=d
            while a and b:
                if a.val<b.val:
                    c.next=a
                    a=a.next
                else:
                    c.next=b
                    b=b.next
                c=c.next
            c.next=a or b
            return d.next

        while len(lists)>1:
            t=[]
            for i in range(0,len(lists),2):
                if i+1<len(lists):
                    t.append(merge(lists[i],lists[i+1]))
                else:
                    t.append(lists[i])
            lists=t

        return lists[0]
