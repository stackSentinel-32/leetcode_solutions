class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        # stack.append(s[0])
        for i in s:
            if stack != [] and stack[-1] != i and i.lower() == stack[-1].lower():
                # if i.lower() == stack[-1].lower():
                    stack.pop()
            else:
                stack.append(i)
                
        return "".join(stack)


