class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # st=0
        # end=st+1
        # res=[]
        # while end < len(prices):
        #     if prices[st] >= prices[end]:
        #         res.append(prices[st]-prices[end])
        #         st+=1         
        #         end=st+1                                                        
        #     else:
        #         end+=1
        
        # while st<len(prices):
        #     res.append(prices[st])
        #     st+=1
        # return res
        
        stack = []
        res = prices[:]

        for i in range(len(prices)):

            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                res[idx] = prices[idx] - prices[i]
                
            stack.append(i)

        return res