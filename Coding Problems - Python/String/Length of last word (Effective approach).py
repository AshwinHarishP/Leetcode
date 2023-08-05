class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Removing spaces at last
        s = s.strip(" ")
        length = 0

        # Traversing from last 
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                length += 1 
            else:
                return length   # If elment has space

        return length       # If length of an element is 1
