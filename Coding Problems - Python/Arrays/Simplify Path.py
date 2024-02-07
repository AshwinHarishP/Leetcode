class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        st = []

        for i in dirs:
            if i == "..":
                if st:
                    st.pop(-1)
            elif i != "." and i:
                st.append(i)
        return "/" + "/".join(st)
