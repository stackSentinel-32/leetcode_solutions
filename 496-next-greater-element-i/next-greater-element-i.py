class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        find={}
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums2[i]:
                stack.pop()
            
            if len(stack)==0:
                find[nums2[i]]=-1
            else:
                find[nums2[i]]=stack[-1]
            
            stack.append(nums2[i])
        
        res=[]
        for x in nums1:
            res.append(find[x])
        return res

