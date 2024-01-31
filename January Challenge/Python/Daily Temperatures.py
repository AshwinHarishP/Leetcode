class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        st = []

        for i, temps in enumerate(temperatures):
            while st and temperatures[st[-1]] < temps:
                ind = st.pop()
                res[ind] = i - ind
            st.append(i)
        return res
        
