class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j=0,0
        stack=[]
        
        while i<len(pushed) or (stack!=[] and j<len(popped)):
            if stack!=[] and popped[j]==stack[-1]:
                stack.pop()
                j+=1
            else:
                if i>=len(pushed):
                    break
                stack.append(pushed[i])
                i+=1
        
        return True if j==len(popped) else False 

        # while i<len(pushed) or (stack!=[] and j<len(popped)):
            
        #     if stack !=[] and stack[-1]==popped[j]:
        #         stack.pop()
        #         j += 1

        #     else:
        #         if i >= len(pushed):
        #             break
        #         stack.append(pushed[i])
        #         i += 1

        # return j==len(popped)
