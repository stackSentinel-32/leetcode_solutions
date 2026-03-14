class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0])
        
        for i in range(1,len(items)):
            items[i][1] = max(items[i][1],items[i-1][1])
        
        def binary_search(price):
            lo,hi = 0,len(items)-1
            result = -1
            while lo <= hi:
                mid = (lo+hi) // 2
                if items[mid][0] <= price:
                    result = mid
                    lo = mid+1
                else:
                    hi = mid-1
            return result
        
        return [items[binary_search(q)][1] if binary_search(q) != -1 else 0 for q in queries]