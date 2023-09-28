class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        array = [0]*len(s)
        for i in range(len(s)):
            array[indices[i]] = s[i]
        return "".join(array)
