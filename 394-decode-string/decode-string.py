class Solution:
    def decodeString(self, s: str) -> str:
        num=""
        stack=[]

        for i in s:
            if i.isdigit():
                num+=i
            
            elif i=="[":
                stack.append(num)
                stack.append(i)
                num=""
            
            elif i.isalpha():
                stack.append(i)
            
            elif i=="]" and stack!=[]:
                ss=""
                while stack[-1] != "[":
                    ss=stack.pop()+ss
                stack.pop()
                
                rep=int(stack.pop())
                ss=ss*rep
                stack.append(ss)

        return "".join(stack)