from collections import Counter,defaultdict
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        
        n=len(items)
        min_price=min(price for fact,price in items)
        
        freq=Counter()
        for fact,price in items:
            freq[fact]+=1
        max_val=max(freq)
        
        free_copy={}
        for fact in freq:
            cnt=0
            ff=fact
            while ff<=max_val:
                cnt+=freq.get(ff,0)
                ff+=fact
            free_copy[fact]=cnt-1
            
        # for i in range(n):
        #     for j in range(n):
        #         if i!=j and (items[j][0] % items[i][0])==0:
        #             free_copy[i]+=1

        cdeal=defaultdict(int)
        for fact,price in items:
            ff=free_copy[fact]
            if ff>0 and price<2*min_price:
                cdeal[price]+=ff

        # cdeal.sort()

        mti=budget//min_price
        curr_cost=0
        tp=0

        for cost in sorted(cdeal):
            cnt=cdeal[cost]
            take=min(cnt,(budget-curr_cost)//cost)
            curr_cost+=take*cost
            tp+=take
            mti=max(mti,2*tp+(budget-curr_cost)//min_price)

        return mti
                     
        #     curr_cost+=cost

        #     if curr_cost>budget:
        #         break

        #     k+=1
        #     tti=(2*k)+(budget-curr_cost)//min_price

        #     if tti>mti:
        #         mti=tti
                
        # return  mti