class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        nums=asteroids
        n =len(nums)
        stack=[]
        
        for i in range(0,n):
            if nums[i]>0:
                stack.append(nums[i])
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(nums[i]):
                    stack.pop()
                
                if len(stack)!=0 and stack[-1]==abs(nums[i]):
                    stack.pop()
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(nums[i])
        return stack

        # stack=[]
        # for i in asteroids:
        #     while stack!=[] and i<0 and stack[-1]>0:
        #         if stack[-1] > abs(i):
        #             break
                
        #         elif stack[-1] == abs(i):
        #             stack.pop()
        #             break

        #         elif stack[-1] < abs(i):
        #             stack.pop()
        #     else:
        #         stack.append(i)

        # return stack