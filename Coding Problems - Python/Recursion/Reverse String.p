class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        def helper(s, start, end):
            # Base Case
            if start >= end:
                return
            # General Case
            s[start], s[end] = s[end], s[start]

            helper(s,start+1, end-1)

        helper(s,start,end)
        
