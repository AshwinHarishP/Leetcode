from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_ele = Counter(nums)
        return any(value > 1 for value in count_ele.values())
