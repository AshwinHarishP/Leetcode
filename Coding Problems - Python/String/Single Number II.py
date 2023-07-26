from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_num = Counter(nums)
        for key,value in count_num.items():
            if value == 1:
                return key
