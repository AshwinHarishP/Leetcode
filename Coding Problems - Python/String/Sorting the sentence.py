class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split(" ")

        words.sort(key = lambda word: word[-1])

        words = " ".join(words)
        res = ""

        for i in range(len(words)):
            if not words[i].isdigit():
                res += words[i]
        return res
