class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        ls = [i for i in count.values()]
        max_val, res = max(ls), 0

        for i in ls:
            if i == max_val:
                res += i
        return res
