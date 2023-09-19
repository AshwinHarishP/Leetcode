class Solution(object):
   
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        store = {}
        
        for i, row in enumerate(mat):
            count = sum(row)
                    
            if count in store: #edit entry
                current = store.get(count)
                store[count] = current + [i]
            else: #create entry
                store[count] = [i]
        
        ans = []
        
        for keys in sorted(store):
            for row in store[keys]:
                ans.append(row)
            
        return ans[:k]


    
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        
        # add all elems
        for i, row in enumerate(mat):
            count = sum(row)
            heapq.heappush(min_heap, [count, i])

        ans = []
        for _ in range(k): # pop k elems
            row = heapq.heappop(min_heap)[1]
            ans.append(row)
            
        return ans
