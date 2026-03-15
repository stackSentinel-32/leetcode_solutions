class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # for i in nums:
        #     hashmap[i] = hashmap.get(i,0)+1
        #     sorted_hashmap=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        # return [i[0] for i in sorted_hashmap[:k]]

        count_lst=[[] for i in range(len(nums)+1)]
        rtn_lst=[]
        
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        
        for key,val in hashmap.items():
            count_lst[val].append(key)
        
        for i in range(len(count_lst)-1,0,-1):
            for j in count_lst[i]:
                if len(rtn_lst)==k:
                    break
                rtn_lst.append(j)
        return rtn_lst


                
        
        