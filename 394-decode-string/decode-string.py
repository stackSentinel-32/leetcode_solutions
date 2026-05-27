class Solution:
    def decodeString(self, s: str) -> str:
#         num=[]
#         stack=[]
#         s=""

#         for i in s:
#             if i.isdigit():
#                 num.append(i)
            
#             elif i=="[" or i.isalpha():
#                 stack.append(i)
            
#             elif i=="]" and stack!=[]:
#                 ss=""
#                 while stack[-1] != "[":
#                     ss = str(stack[-1]) + ss
#                     for i in range(num[-1]-1):
#                         s+=ss
#                     stack.pop()
#                 else:
#                     stack.pop()

#         return s

        num=""
        stack=[]

        for i in s:
            if i.isdigit():
                num += i

            elif i == "[":
                stack.append(num)
                stack.append(i)
                num = ""

            elif i.isalpha():
                stack.append(i)

            elif i == "]":

                ss = ""
                while stack[-1] != "[":
                    ss = stack.pop() + ss

                stack.pop() 

                repeat = int(stack.pop())
                stack.append(ss * repeat)

        return "".join(stack)