class Solution:
    def sortableIntegers(self,nums:List[int])->int:
        n=len(nums)
        pf_mx=[0]*(n+1)
        sf_mn=[10**9]*(n+1)
        pref_drop=[0]*n

        for i,x in enumerate(nums):
            pf_mx[i+1]=max(pf_mx[i],x)

        for i in range(n-1,-1,-1):
            sf_mn[i]=min(nums[i],sf_mn[i+1])

        for i in range(1,n):
            pref_drop[i]=pref_drop[i-1]+(nums[i-1]>nums[i])

        def check(k):
            for st in range(0,n,k):
                end=st+k-1
                drops=pref_drop[end]-pref_drop[st]

                if nums[end]>nums[st]:
                    drops+=1

                if drops>1 or pf_mx[st]>sf_mn[st]:
                    return False
            return True

        res=0
        for k in range(1,n+1):
            if n%k==0 and check(k):
                res+=k
        return res