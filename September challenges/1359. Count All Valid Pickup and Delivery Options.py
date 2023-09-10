from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
import math
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f

mod = 10**9 + 7
memo = {1: 1, 2: 6}
for j in range(3, 501):
    memo[j] = j * (memo[j - 1] * (2 * j - 1)) % mod

class Solution:
    def countOrders(self, n: int) -> int:
        return memo[n]


sol = Solution()
for i in range(1, 5):
    print(i, sol.countOrders(i))
