class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)
        # while len(self.stack1) > 0:
        #     self.stack2.append(self.stack1.pop())
        
        # self.stack1.append(x)

        # while len(self.stack2) > 0:
        #     self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        
        poppy=self.stack2.pop()

        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())
 
        return poppy 
        # x=self.stack1[-1]
        # self.stack1.pop()
        # return x


    def peek(self) -> int:
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        
        peek=self.stack2[-1]

        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())
         
        return peek

    def empty(self) -> bool:
        return len(self.stack1)==0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()