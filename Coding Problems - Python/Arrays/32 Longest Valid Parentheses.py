class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        st = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                max_len = max(max_len, i - st[-1]) 
        return max_len
