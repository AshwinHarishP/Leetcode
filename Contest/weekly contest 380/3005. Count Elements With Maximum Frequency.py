from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_value = 0
        
        for key,value in cnt.items():
            if value > max_value:
                max_value = value
                
        if max_value == 1:
            return len(nums)
        
        res = 0
        
        for _, value in cnt.items():
            if value == max_value:
                res += value
        return res
