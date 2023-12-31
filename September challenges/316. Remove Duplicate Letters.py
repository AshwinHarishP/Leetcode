class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = collections.Counter(s)
        stack = []
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and cnt[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            cnt[c] -= 1
        return "".join(stack)
