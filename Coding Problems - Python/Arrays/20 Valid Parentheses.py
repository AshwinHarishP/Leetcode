class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        st = []

        for i in s:
            if i in hashmap:
                st.append(i)
            else:
                if st and hashmap[st[-1]] == i:

                    st.pop()
                else:
                    return 0
        if st:
            return 0
        return 1
