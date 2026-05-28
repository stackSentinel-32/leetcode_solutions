class Node:
    def __init__(self , val):
        self.val=val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.n=0

    def get(self, index: int) -> int:
        if index<0 or index>=self.n:
            return -1
        curr=self.head
        pos=0
        while curr!=None:
            if pos==index:
                return curr.val
                break
            curr=curr.next
            pos+=1

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        self.n+=1

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.n+=1
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        self.n+=1

    def addAtIndex(self, index: int, val: int) -> None:
        new_node=Node(val)

        if index<0 or index>self.n:
            return 
        
        if index==0:
            self.addAtHead(val)
            return

        curr=self.head
        for i in range(index-1):
            curr=curr.next
        new_node.next=curr.next
        curr.next=new_node
        self.n+=1
            
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.n:
            return 
        if index==0:
            self.head=self.head.next
            self.n-=1
            return 

        curr=self.head
        for i in range(index-1):
            curr=curr.next
        curr.next=curr.next.next
        self.n-=1
        
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)