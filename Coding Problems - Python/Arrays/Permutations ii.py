from typing import List
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_permutations = set(permutations(nums))
        return [list(perm) for perm in unique_permutations]
