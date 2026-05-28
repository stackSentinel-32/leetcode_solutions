class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
       self.curr=Node(homepage)

    def visit(self, url: str) -> None:
        # self.history=self.history[:self.curr+1]
        # self.history.append(url)
        # self.curr+=1
        new_node=Node(url)
        self.curr.next=new_node
        new_node.prev=self.curr
        self.curr=new_node

    def back(self, steps: int) -> str:
        # self.curr=max(0,self.curr-steps)
        # return self.history[self.curr]
        while steps>0 and self.curr.prev:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val

    def forward(self, steps: int) -> str:
        # self.curr=min(len(self.history)-1,self.curr+steps)
        # return self.history[self.curr]
        while steps>0 and self.curr.next!=None:
            self.curr=self.curr.next
            steps-=1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)