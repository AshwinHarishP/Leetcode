class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        i = len(s) - 1
        return_str = ""
        while i >= 0:
            if s[i] != "":
                return_str += s[i] +" "
                i -= 1
            else:
                i -= 1

        return return_str.strip(" ")
