class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip(" ")
        k = 0
        for i in range(len(s)):
            if s[i] == " ":
                k = 0
            else:
                k += 1

        return k
