class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        Str = ""

        while i <= len(word1) - 1  or j <= len(word2) - 1 :
    
            if i <= len(word1) - 1:
                Str += word1[i]
                i += 1
            if j <= len(word2) - 1:
                Str += word2[j]
                j += 1

        return Str
