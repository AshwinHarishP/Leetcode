from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        diff = Counter(t) - Counter(s)

        for key, value in diff.items():
            return key
        
