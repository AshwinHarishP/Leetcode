class Solution(object):
    def findTheDifference(self, s, t):
        diff = 0
        for char in s+t:
            diff ^= ord(char)
        return chr(diff)

        
