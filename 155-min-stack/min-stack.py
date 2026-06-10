class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

        # self.mn=float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if val<self.mn:
        #     self.mn=min(self.mn,val)
        if len(self.minStack)==0 or val<=self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        poppy=self.stack.pop()
        if poppy==self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        # mn=float('inf')
        # for i in range(len(self.stack)):
        #     if self.stack[i] < mn:
        #         mn=self.stack[i]
        # return mn

class MinStack:
    def __init__(self):
        self.stack=[]
    
    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append([val,val])
        else:
            mn=min(self.stack[-1][1],val)
            self.stack.append([val,mn])
    
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]    

    def getMin(self) -> int:
        return self.stack[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()